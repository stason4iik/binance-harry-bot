import asyncio
import hashlib

from monitor import get_latest_post
from translator import translate_text
from telegram_bot import send_message
from database import (
    init_db,
    is_new_post,
    save_post
)


async def main():

    await init_db()

    print("Проверка новых постов...")

    post_text = await get_latest_post()

    if not post_text:
        print("Постов нет")
        return


    post_id = hashlib.md5(
        post_text.encode()
    ).hexdigest()


    if await is_new_post(post_id):

        await save_post(post_id)

        print("Новый пост найден")


        translated = translate_text(
            post_text
        )


        message = (
            "🚨 <b>Harry Liu новый пост</b>\n\n"
            "🇷🇺 <b>Перевод:</b>\n\n"
            f"{translated}\n\n"
            "────────────\n"
            "Источник: Binance Square"
        )


        await send_message(
            message
        )

    else:
        print("Новых постов нет")



if __name__ == "__main__":

    asyncio.run(main())
