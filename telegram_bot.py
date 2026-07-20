from telegram import Bot
from config import TELEGRAM_TOKEN, TELEGRAM_ID


async def send_message(text):
    bot = Bot(token=TELEGRAM_TOKEN)

    await bot.send_message(
        chat_id=TELEGRAM_ID,
        text=text,
        parse_mode="HTML"
    )