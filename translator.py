from openai import OpenAI
from config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def translate_text(text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":
                "Переводи криптовалютные новости на русский язык. "
                "Сохраняй названия монет, тикеры и важные детали."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content