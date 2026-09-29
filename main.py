from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from bot.handlers import start, status


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))

    application.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex("^🖥 Просмотр статуса сервера$"),
            status
        )
    )

    print("Telegram-бот запущен!")

    application.run_polling()


if __name__ == "__main__":
    main()