from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from monitor.metrics import get_all_metrics
from monitor.alerts import check_thresholds


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🖥 Просмотр статуса сервера"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Привет! Я бот для мониторинга Debian-сервера.\n\n"
        "Выбери действие:",
        reply_markup=reply_markup
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    metrics = get_all_metrics()

    alerts = check_thresholds(metrics)

    text = (
        "🖥 СТАТУС СЕРВЕРА\n\n"
        f"⚙️ CPU: {metrics['cpu']}%\n"
        f"🧠 RAM: {metrics['ram']}%\n"
        f"💾 Диск: {metrics['disk']}%\n"
        f"🌐 Соединения: {metrics['connections']}\n"
    )

    if alerts:
        text += "\n⚠️ ПРЕДУПРЕЖДЕНИЯ:\n"
        text += "\n".join(alerts)
    else:
        text += "\n🟢 Все показатели в норме"

    await update.message.reply_text(text)