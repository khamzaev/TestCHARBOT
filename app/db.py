from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import POSTGRES_URL

# Создаем базовый класс для моделей
Base = declarative_base()

# Настройка асинхронного движка подключения
engine = create_async_engine(POSTGRES_URL, echo=True)

# Создаем фабрику сессий
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Функция для инициализации таблиц
async def init_db():
    async with engine.begin() as conn:
        # Создаем таблицы
        await conn.run_sync(Base.metadata.create_all)
