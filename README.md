# Debian Server Monitor Bot

Telegram-бот для мониторинга состояния Debian Linux-сервера.

Бот позволяет вручную получить текущую информацию о загрузке сервера через Telegram.

## Возможности

- 🖥 Просмотр состояния сервера через Telegram
- ⚙️ Мониторинг загрузки CPU
- 🧠 Мониторинг использования RAM
- 💾 Мониторинг использования диска
- 🌐 Подсчёт сетевых соединений
- ⚠️ Проверка показателей по установленным порогам
- 🟢 Отображение сообщения, если все показатели находятся в пределах нормы

## Используемые технологии

- Python 3
- python-telegram-bot
- psutil
- python-dotenv
- Debian Linux
- Git / GitHub

## Структура проекта

```text
server-monitor-bot/
├── bot/
│   ├── __init__.py
│   ├── handlers.py
│   └── messages.py
├── monitor/
│   ├── __init__.py
│   ├── metrics.py
│   └── alerts.py
├── config.py
├── main.py
├── .env
├── .env.example
├── .gitignore
├── README.md
└── venv/