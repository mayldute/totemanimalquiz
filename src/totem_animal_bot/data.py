from .models import AnimalResult, Answer, Question


QUESTIONS = (
    Question(
        text="Where would you like to live?",
        answers=(
            Answer(
                text="In the forest",
                points={"East Siberian Lynx": 3, "Snow Leopard": 2},
            ),
            Answer(text="In the steppe", points={"Grevy's Zebra": 3}),
            Answer(
                text="By the river",
                points={"European Otter": 2, "Mute Swan": 3},
            ),
            Answer(text="In the mountains", points={"Snow Leopard": 3}),
        ),
        image_url=(
            "https://i.pinimg.com/474x/ac/b3/35/"
            "acb335a3a3fc4e6a2da1f6cd9cc37db7.jpg"
        ),
    ),
    Question(
        text="What is your favorite food?",
        answers=(
            Answer(
                text="Fruits and vegetables",
                points={"Grevy's Zebra": 2, "European Otter": 3},
            ),
            Answer(text="Fish", points={"European Otter": 3}),
            Answer(
                text="Meat",
                points={"East Siberian Lynx": 3, "Snow Leopard": 2},
            ),
            Answer(text="Grain", points={"Mute Swan": 3}),
        ),
        image_url=(
            "https://i.pinimg.com/474x/14/b4/5b/"
            "14b45b1b8880986cb36628ec37594f00.jpg"
        ),
    ),
    Question(
        text="How do you prefer to spend your free time?",
        answers=(
            Answer(text="In peace and reflection", points={"Mute Swan": 3}),
            Answer(
                text="Playing active games",
                points={"European Otter": 2, "Grevy's Zebra": 3},
            ),
            Answer(
                text="Exploring nature",
                points={"Snow Leopard": 3, "East Siberian Lynx": 2},
            ),
            Answer(text="In a comfort zone", points={"African Penguin": 3}),
        ),
        image_url=(
            "https://i.pinimg.com/736x/16/7c/1e/"
            "167c1e9b4b981fcdbdf48219da3b8933.jpg"
        ),
    ),
    Question(
        text="What is your personality like?",
        answers=(
            Answer(text="Patient and caring", points={"Amur Tiger": 3}),
            Answer(
                text="Energetic and curious",
                points={"European Otter": 2, "Grevy's Zebra": 3},
            ),
            Answer(
                text="Independent and a bit mysterious",
                points={"East Siberian Lynx": 3, "Snow Leopard": 2},
            ),
            Answer(text="Calm and majestic", points={"Mute Swan": 3}),
        ),
        image_url=(
            "https://i.pinimg.com/736x/5c/ac/5a/"
            "5cac5a9ca9ea765671b446a7480f09f9.jpg"
        ),
    ),
    Question(
        text="How do you feel about company?",
        answers=(
            Answer(text="I prefer to be alone", points={"Amur Tiger": 3}),
            Answer(
                text="I like company, but not always",
                points={"Snow Leopard": 2},
            ),
            Answer(
                text="I love being surrounded by others",
                points={"European Otter": 3, "Grevy's Zebra": 2},
            ),
            Answer(
                text="I'm always with friends and family",
                points={"African Penguin": 3},
            ),
        ),
        image_url=(
            "https://i.pinimg.com/736x/2a/a3/21/"
            "2aa3219150c693f022adc0e5dda06ef7.jpg"
        ),
    ),
    Question(
        text="What lifestyle suits you best?",
        answers=(
            Answer(
                text="I love traveling and exploring",
                points={"Snow Leopard": 3, "Amur Tiger": 2},
            ),
            Answer(
                text="I prefer to relax at home",
                points={"African Penguin": 2, "Mute Swan": 3},
            ),
            Answer(
                text="I enjoy active hobbies",
                points={"European Otter": 3, "Grevy's Zebra": 2},
            ),
            Answer(
                text="I always find time for myself",
                points={"Amur Leopard": 3},
            ),
        ),
        image_url=(
            "https://i.pinimg.com/474x/d5/f2/42/"
            "d5f24202a391168ab2f52220f92da7f8.jpg"
        ),
    ),
    Question(
        text="How do you feel about cold weather?",
        answers=(
            Answer(
                text="I like the cold and feel comfortable in frost",
                points={"African Penguin": 3, "Snow Leopard": 2},
            ),
            Answer(
                text="Cold isn't for me; I prefer warmth",
                points={"European Otter": 2, "Amur Leopard": 3},
            ),
            Answer(
                text="I can adapt to any weather",
                points={"Grevy's Zebra": 3},
            ),
            Answer(
                text="I prefer moderate conditions",
                points={"Amur Tiger": 3, "Mute Swan": 2},
            ),
        ),
        image_url=(
            "https://i.pinimg.com/474x/fa/60/9e/"
            "fa609ef81a8ee80bf6516eed87324b3a.jpg"
        ),
    ),
)


RESULTS = {
    "East Siberian Lynx": AnimalResult(
        name="East Siberian Lynx",
        description=(
            "You are an East Siberian Lynx! Independent and secretive. "
            "You love solitude, and your grace and strength impress those "
            "around you. You know what you want and do not give up when "
            "things become difficult."
        ),
        image_url=(
            "https://i.pinimg.com/474x/39/84/bc/"
            "3984bce43f624988048b03fc5b8ddb10.jpg"
        ),
        details_url=(
            "https://moscowzoo.ru/animals/kinds/vostochno_sibirskaya_rys"
        ),
    ),
    "Snow Leopard": AnimalResult(
        name="Snow Leopard",
        description=(
            "You are a Snow Leopard! A free-spirited explorer. You are brave, "
            "independent, and always ready to reach new heights."
        ),
        image_url=(
            "https://i.pinimg.com/474x/95/cd/e0/"
            "95cde05f94637d018e1874e985281441.jpg"
        ),
        details_url="https://moscowzoo.ru/animals/kinds/irbis_snezhnyy_bars",
    ),
    "Grevy's Zebra": AnimalResult(
        name="Grevy's Zebra",
        description=(
            "You are Grevy's Zebra! Energetic, friendly, adaptable, and ready "
            "for any adventure."
        ),
        image_url=(
            "https://i.pinimg.com/474x/28/58/29/"
            "285829f5368356af685e75fe8a67debf.jpg"
        ),
        details_url="https://moscowzoo.ru/animals/kinds/zebra_grevi",
    ),
    "European Otter": AnimalResult(
        name="European Otter",
        description=(
            "You are a European Otter! Curious, playful, and always looking for "
            "new experiences. Your joy and friendliness cheer people up."
        ),
        image_url=(
            "https://i.pinimg.com/474x/96/2a/4d/"
            "962a4d60cbb4ed2e5e0c6ff81a7d909a.jpg"
        ),
        details_url="https://moscowzoo.ru/animals/kinds/obyknovennaya_vydra",
    ),
    "Mute Swan": AnimalResult(
        name="Mute Swan",
        description=(
            "You are a Mute Swan! Calm, graceful, and strong. You appreciate "
            "harmony and beauty and remain composed in difficult situations."
        ),
        image_url=(
            "https://i.pinimg.com/474x/5b/9d/85/"
            "5b9d85394d391ed3f17e38c2bdf5ecd2.jpg"
        ),
        details_url="https://moscowzoo.ru/animals/kinds/lebed_shipun",
    ),
    "Amur Tiger": AnimalResult(
        name="Amur Tiger",
        description=(
            "You are an Amur Tiger! Powerful, brave, determined, and loyal to "
            "the people you trust."
        ),
        image_url=(
            "https://i.pinimg.com/474x/20/a2/30/"
            "20a230452438e019fcb159ee08592cb9.jpg"
        ),
        details_url="https://moscowzoo.ru/animals/kinds/amurskiy_tigr",
    ),
    "African Penguin": AnimalResult(
        name="African Penguin",
        description=(
            "You are an African Penguin! Optimistic, resilient, sociable, and "
            "always ready to work as part of a team."
        ),
        image_url=(
            "https://i.pinimg.com/474x/5d/06/ae/"
            "5d06aefb04b6cfe94790dea743274ca7.jpg"
        ),
        details_url=(
            "https://moscowzoo.ru/animals/kinds/pingvin_afrikanskiy_ochkovyy"
        ),
    ),
    "Amur Leopard": AnimalResult(
        name="Amur Leopard",
        description=(
            "You are an Amur Leopard! Quiet, precise, confident, and strong. "
            "You face challenges calmly and act with purpose."
        ),
        image_url=(
            "https://i.pinimg.com/474x/70/c9/f7/"
            "70c9f722a23843af40324d74a847dc5d.jpg"
        ),
        details_url=(
            "https://moscowzoo.ru/animals/kinds/dalnevostochnyy_leopard"
        ),
    ),
}
