import os
from telegram.ext import Updater, CommandHandler
import random

QUOTES = [
    "The unexamined life is not worth living. — Socrates",
    "Happiness depends upon ourselves. — Aristotle",
    "He who thinks great thoughts, often makes great errors. — Martin Heidegger",
    "Man is condemned to be free. — Jean-Paul Sartre",
    "Whereof one cannot speak, thereof one must be silent. — Ludwig Wittgenstein"
]

def start(update, context):
    update.message.reply_text("Welcome! Use /quote to get a philosophical quote.")

def quote(update, context):
    update.message.reply_text(random.choice(QUOTES))

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is not set in environment variables")
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quote", quote))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
