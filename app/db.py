from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import sessionmaker
from sqlalchemy.orm import declarative_base

from config import POSTGRES_URL


# Создаем базовый класс для моделей
Base = declarative_base()

# Настройка асинхронного движка подключения
engine = create_async_engine(POSTGRES_URL, echo=True)

# Создаем фабрику сессий (асинхронно)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Функция для инициализации базы данных
async def init_db():
    async with engine.begin() as conn:
        # Создаем таблицы
        await conn.run_sync(Base.metadata.create_all)
