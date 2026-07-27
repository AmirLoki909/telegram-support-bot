import os
from dotenv import load_dotenv

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📨 ارسال پیام"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "سلام 👋\n"
        "به پشتیبانی خوش آمدید.\n"
        "برای ارسال پیام روی دکمه زیر بزنید.",
        reply_markup=reply_markup
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    print(
        f"پیام جدید از {user.first_name} ({user.id}): "
        f"{update.message.text}"
    )

    await update.message.reply_text(
        "پیام شما دریافت شد ✅\n"
        "به زودی پاسخ می‌دهیم."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("Bot started...")

    app.run_polling()


if __name__ == "__main__":
    main()
