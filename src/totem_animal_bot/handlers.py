import logging

from telebot import TeleBot
from telebot.types import CallbackQuery, Message

from .cache import ImageCache
from .config import Settings
from .data import QUESTIONS, RESULTS
from .keyboards import (
    create_back_keyboard,
    create_question_keyboard,
    create_result_keyboard,
    create_share_keyboard,
    create_welcome_keyboard,
)
from .quiz import EmptyScoreError, add_points, determine_result
from .state import UserStateStorage

logger = logging.getLogger(__name__)

WELCOME_TEXT = """Hello!

Welcome to the Totem Animal Quiz! 🐾
Answer seven questions to discover which Moscow Zoo animal best matches your personality.

You can also learn more about the zoo's guardianship program after completing the quiz."""


def register_handlers(
    bot: TeleBot,
    *,
    settings: Settings,
    storage: UserStateStorage,
    image_cache: ImageCache,
) -> None:
    def get_result(chat_id: int):
        state = storage.get(chat_id)
        if state is None:
            return None
        try:
            animal = determine_result(state.scores)
        except EmptyScoreError:
            return None
        return RESULTS[animal]

    def send_question(chat_id: int) -> None:
        state = storage.get_or_create(chat_id)
        if state.current_question >= len(QUESTIONS):
            send_result(chat_id)
            return

        question = QUESTIONS[state.current_question]
        answer_texts = tuple(answer.text for answer in question.answers)
        bot.send_photo(
            chat_id,
            image_cache.get_image(question.image_url),
            caption=question.text,
            reply_markup=create_question_keyboard(
                state.current_question,
                answer_texts,
            ),
        )

    def send_result(chat_id: int) -> None:
        result = get_result(chat_id)
        if result is None:
            bot.send_message(chat_id, "Send /start to begin the quiz.")
            return

        caption = (
            f"{result.description}\n\n"
            f'<a href="{result.details_url}">Learn more about this animal</a>'
        )
        bot.send_photo(
            chat_id,
            image_cache.get_image(result.image_url),
            caption=caption,
            reply_markup=create_result_keyboard(),
            parse_mode="HTML",
        )

    @bot.message_handler(commands=["start"])
    def send_welcome(message: Message) -> None:
        storage.reset(message.chat.id)
        bot.send_message(
            message.chat.id,
            WELCOME_TEXT,
            reply_markup=create_welcome_keyboard(),
        )

    @bot.callback_query_handler(func=lambda call: call.data == "start_quiz")
    def start_quiz(call: CallbackQuery) -> None:
        chat_id = call.message.chat.id
        bot.answer_callback_query(call.id)
        storage.reset(chat_id)
        send_question(chat_id)

    @bot.callback_query_handler(
        func=lambda call: bool(call.data and call.data.startswith("answer:"))
    )
    def handle_answer(call: CallbackQuery) -> None:
        bot.answer_callback_query(call.id)
        chat_id = call.message.chat.id
        state = storage.get(chat_id)

        if state is None:
            bot.send_message(
                chat_id,
                "Your quiz session expired. Send /start to begin again.",
            )
            return

        try:
            _, question_value, answer_value = call.data.split(":")
            question_index = int(question_value)
            answer_index = int(answer_value)
        except (AttributeError, ValueError):
            logger.warning("Invalid answer callback: %r", call.data)
            return

        if question_index != state.current_question:
            return

        try:
            answer = QUESTIONS[question_index].answers[answer_index]
        except IndexError:
            logger.warning("Invalid question or answer index in %r", call.data)
            return

        add_points(state.scores, answer.points)
        state.current_question += 1
        storage.touch(chat_id)
        send_question(chat_id)

    @bot.callback_query_handler(func=lambda call: call.data == "share_menu")
    def share_menu(call: CallbackQuery) -> None:
        bot.answer_callback_query(call.id)
        result = get_result(call.message.chat.id)
        if result is None:
            bot.send_message(call.message.chat.id, "Complete the quiz first.")
            return

        bot.edit_message_reply_markup(
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_share_keyboard(
                animal=result.name,
                bot_username=settings.bot_username,
            ),
        )

    @bot.callback_query_handler(func=lambda call: call.data == "back_to_result")
    def back_to_result(call: CallbackQuery) -> None:
        bot.answer_callback_query(call.id)
        result = get_result(call.message.chat.id)
        if result is None:
            bot.send_message(call.message.chat.id, "Complete the quiz first.")
            return

        if call.message.caption:
            bot.edit_message_reply_markup(
                call.message.chat.id,
                call.message.message_id,
                reply_markup=create_result_keyboard(),
            )
        else:
            send_result(call.message.chat.id)

    @bot.callback_query_handler(func=lambda call: call.data == "contact_support")
    def contact_support(call: CallbackQuery) -> None:
        bot.answer_callback_query(call.id)
        chat_id = call.message.chat.id
        bot.send_message(chat_id, "Write your question in one message.")
        bot.register_next_step_handler_by_chat_id(chat_id, forward_to_admin)

    def forward_to_admin(message: Message) -> None:
        username = message.from_user.username or "no_username"
        result = get_result(message.chat.id)
        result_name = result.name if result is not None else "No result"
        bot.send_message(
            settings.admin_id,
            (
                f"📩 New support request from @{username}\n\n"
                f"Quiz result: {result_name}\n\n"
                f"Message: {message.text or '[non-text message]'}"
            ),
        )
        bot.send_message(
            message.chat.id,
            "Your question has been sent to the administrator.",
            reply_markup=create_back_keyboard(),
        )

    @bot.callback_query_handler(func=lambda call: call.data == "leave_feedback")
    def ask_feedback(call: CallbackQuery) -> None:
        bot.answer_callback_query(call.id)
        chat_id = call.message.chat.id
        bot.send_message(chat_id, "Write your feedback in one message.")
        bot.register_next_step_handler_by_chat_id(chat_id, forward_feedback)

    def forward_feedback(message: Message) -> None:
        username = message.from_user.username or "no_username"
        bot.send_message(
            settings.admin_id,
            (
                f"📝 New feedback from @{username}\n\n"
                f"{message.text or '[non-text message]'}"
            ),
        )
        bot.send_message(
            message.chat.id,
            "Thank you for your feedback! 😊",
            reply_markup=create_back_keyboard(),
        )
