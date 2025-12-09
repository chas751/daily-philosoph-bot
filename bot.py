import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import random

# ========= ТВОЙ ТОКЕН =========
TELEGRAM_BOT_TOKEN = "8228885470:AAFxS7h1Y5bYxSyjhAVG7FIahdSaJCoESBs"

# ========= РЕКВИЗИТЫ =========
VTB_CARD = "2200 2460 3013 9912"
TRX_WALLET = "TErjzxxbTg1uvhEDBzpnvDr2p3g1RRw5Pd"

# ========= ЦИТАТЫ =========
QUOTES = [
    "Мудрость начинается с удивления.",
    "Мы становимся тем, о чём думаем.",
    "Человек — это то, что он делает."
]

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# /start
@dp.message(Command("start"))
async def start(message: Message):
    text = (
        "Привет! Я философский бот.\n\n"
        "💬 Напиши /quote чтобы получить цитату.\n\n"
        "💵 *Донаты:*\n"
        f"💳 ВТБ: `{VTB_CARD}`\n"
        f"🔗 USDT (TRC20): `{TRX_WALLET}`"
    )
    await message.answer(text, parse_mode="Markdown")

# /quote
@dp.message(Command("quote"))
async def quote(message: Message):
    await message.answer(random.choice(QUOTES))

async def main():
    print("BOT STARTED...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
