from aiogram import Router, types, Bot
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from app import logger
from app.services.data_service import DataService
from injectable import autowired, Autowired


router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    """
    Обработчик команды /start.

    Отправляет приветственное сообщение с интерактивной кнопкой для получения данных.

    :param message: Сообщение от пользователя.
    """
    logger.info(f"User {message.from_user.id} initiated /start command")
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Fetch Data", callback_data="fetch_data")]
        ]
    )
    await message.answer("Welcome! Use the button below to fetch data.", reply_markup=keyboard)


@router.callback_query(lambda c: c.data == "fetch_data")
@autowired
async def fetch_data_callback(
    callback: CallbackQuery,
    bot: Bot,
    data_service: Autowired(DataService)
):
    """
    Обработчик нажатия на кнопку "Fetch Data".

    Выполняет запрос к API, сохраняет данные в базу данных и Google Sheets, а также уведомляет пользователя
    о результате выполнения.

    :param callback: Callback-запрос от кнопки.
    :param bot: Экземпляр бота.
    :param data_service: Сервис для работы с данными.
    """
    try:
        logger.info(f"User {callback.from_user.id} requested data fetch")
        data = await data_service.fetch_and_process_data("posts")
        await data_service.save_data([item.dict() for item in data])
        await data_service.save_to_google_sheets("Sheet1", data)
        logger.info(f"Data successfully processed for user {callback.from_user.id}")
        await callback.message.answer("Data successfully fetched, saved to DB and Google Sheets!")
    except Exception as e:
        logger.error(f"Error for user {callback.from_user.id}: {e}")
        await callback.message.answer(f"An error occurred: {str(e)}")
