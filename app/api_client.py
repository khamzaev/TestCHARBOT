import aiohttp
from app import logger
from app.utils import transform_keys
from injectable import injectable


@injectable
class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    async def fetch_data(self, endpoint: str):
        """
        Выполняет запрос к API и возвращает данные в формате snake_case.

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
