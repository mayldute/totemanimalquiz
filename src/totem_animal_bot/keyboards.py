from urllib.parse import quote

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

GUARDIANSHIP_URL = "https://moscowzoo.ru/about/guardianship"


def create_welcome_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Start Quiz", callback_data="start_quiz"))
    markup.add(
        InlineKeyboardButton(
            "About the Guardianship Program",
            url=GUARDIANSHIP_URL,
        )
    )
    return markup


def create_question_keyboard(
    question_index: int,
    answer_texts: tuple[str, ...],
) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for answer_index, answer_text in enumerate(answer_texts):
        markup.add(
            InlineKeyboardButton(
                answer_text,
                callback_data=f"answer:{question_index}:{answer_index}",
            )
        )
    return markup


def create_result_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Try Again", callback_data="start_quiz"))
    markup.add(
        InlineKeyboardButton("Become a Guardian", url=GUARDIANSHIP_URL),
        InlineKeyboardButton("📢 Share", callback_data="share_menu"),
    )
    markup.add(
        InlineKeyboardButton("Leave Feedback", callback_data="leave_feedback"),
        InlineKeyboardButton("Contact Support", callback_data="contact_support"),
    )
    return markup


def create_back_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Back", callback_data="back_to_result"))
    return markup


def create_share_keyboard(
    *,
    animal: str,
    bot_username: str,
) -> InlineKeyboardMarkup:
    bot_url = f"https://t.me/{bot_username}"
    message = (
        f"I took the quiz and discovered my totem animal: {animal}! 🐾\n\n"
        f"Take the quiz: {bot_url}"
    )
    encoded_message = quote(message)
    encoded_url = quote(bot_url, safe="")

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            "Share on X",
            url=f"https://twitter.com/intent/tweet?text={encoded_message}",
        ),
        InlineKeyboardButton(
            "Share on Telegram",
            switch_inline_query=message,
        ),
    )
    markup.add(
        InlineKeyboardButton(
            "Share on Facebook",
            url=(
                "https://www.facebook.com/sharer/sharer.php"
                f"?u={encoded_url}"
            ),
        )
    )
    markup.add(InlineKeyboardButton("🔙 Back", callback_data="back_to_result"))
    return markup
