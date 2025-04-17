from aiogram import Bot, Dispatcher
from aiohttp import web
from app.bot.handlers import register_handlers
from app.database.connection import init_db


API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Укажите ваш токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Инициализация базы данных
init_db()

# Регистрация хендлеров
register_handlers(dp)

# Вебхук обработчик
async def handle_webhook(request):
    update = await request.json()
    await dp.process_update(update)
    return web.Response()

# Запуск aiohttp-сервера
def main():
    app = web.Application()
    app.router.add_post("/webhook", handle_webhook)

    print("Бот запущен!")
    web.run_app(app, port=8080)

if __name__ == "__main__":
    main()
