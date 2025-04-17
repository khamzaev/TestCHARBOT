from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web
from config import TELEGRAM_API_TOKEN

from app.infrastructure.db import init_db
from app.handlers import start
from app.infrastructure.di_container import configure_di


# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()

# Регистрация хендлеров
dp.include_router(start.router)


@dp.startup()
async def on_startup(app: web.Application):
    """
    Выполняется при запуске приложения.
    """
    await init_db()  # Инициализация базы данных
    configure_di()  # Настройка контейнера зависимостей
    await bot.set_webhook(url=f"https://your-domain.com/webhook")


async def on_shutdown(app: web.Application):
    """
    Выполняется при остановке приложения.
    """
    await bot.delete_webhook()


# Инициализация веб-приложения
app = web.Application()
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

# Настройка маршрутов для вебхуков
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")


# Запуск приложения
if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
