import aiohttp
from injectable import injectable

from app import logger
from app.utils import transform_keys


@injectable
class APIClient:
    """
    Клиент для работы с API.
    """
    BASE_URL = "https://jsonplaceholder.typicode.com"

    async def fetch_data(self, endpoint: str):
        """
        Выполняет запрос к API и возвращает данные с преобразованными ключами.

        :param endpoint: Конечная точка API (например, 'users', 'posts').
        :return: Данные с преобразованными ключами.
        """
        try:
            logger.info(f"Запрос данных с API: {self.BASE_URL}/{endpoint}")
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.BASE_URL}/{endpoint}") as response:
                    response.raise_for_status()
                    data = await response.json()
                    logger.info(f"Данные успешно получены с API: {endpoint}")
                    return transform_keys(data)
        except Exception as e:
            logger.error(f"Ошибка при запросе данных с API: {e}")
            raise
