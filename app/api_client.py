from injectable import injectable
import aiohttp
from app import logger


@injectable
class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    async def fetch_data(self, endpoint: str):
        try:
            logger.info(f"Fetching data from API: {self.BASE_URL}/{endpoint}")
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.BASE_URL}/{endpoint}") as response:
                    response.raise_for_status()
                    data = await response.json()
                    logger.info(f"Data successfully fetched from API: {endpoint}")
                    return data
        except Exception as e:
            logger.error(f"Error fetching data from API: {e}")
            raise