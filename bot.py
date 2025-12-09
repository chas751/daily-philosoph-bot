
import os
import sqlite3
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

# ============================
# ВС8228885470:AAFxS7h1Y5bYxSyjhAVG7FIahdSaJCoESBsТАВЬТЕ СВОЙ ТОКЕН СЮДА
# ============================
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"8228885470:AAFxS7h1Y5bYxSyjhAVG7FIahdSaJCoESBs

# Реквизиты
VTB_CARD = "YOUR_VTB_CARD"2200 2460 3013 9912
TRX_WALLET = "TErjzxxbTg1uvhEDBzpnvDr2p3g1RRw5Pd"

DB_PATH = "quotes.db"

def get_random_quote():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT text FROM quotes ORDER BY RANDOM() LIMIT 1;")
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0]
    return "Цитаты в базе отсутствуют."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Привет! Я философский бот.\"" + "\n\n" +
        "💳 *Карта ВТБ:* `" + VTB_CARD + "`\n" +
        "🔗 *USDT (TRC20):* `" + TRX_WALLET + "`\n"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_random_quote())

async def send_daily_quote(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.data["chat_id"]
    await context.bot.send_message(chat_id, get_random_quote())

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    context.job_queue.run_daily(
        send_daily_quote,
        time=datetime.time(hour=9, minute=0),
        data={"chat_id": chat_id},
        name=f"daily_{chat_id}"
    )
    await update.message.reply_text("Вы подписались на ежедневные цитаты!")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("subscribe", subscribe))

    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
