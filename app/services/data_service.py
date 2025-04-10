from app import logger
from typing import List
from app.api_client import APIClient
from app.models.data_model import APIData
from app.utils import transform_keys
from app.google_sheets_client import GoogleSheetsClient
from injectable import injectable, autowired, Autowired
from sqlalchemy.ext.asyncio import AsyncSession


@injectable
class DataService:
    @autowired
    def __init__(
            self,
            db_session: AsyncSession,
            api_client: Autowired(APIClient),
            google_sheets_client: Autowired(GoogleSheetsClient)
    ):
        self.db_session = db_session
        self.api_client = APIClient()
        self.google_sheets_client = google_sheets_client


    async def fetch_and_process_data(self, endpoint: str) -> List[APIData]:
        try:
            logger.info(f"Fetching and processing data from API: {endpoint}")
            raw_data = await self.api_client.fetch_data(endpoint)
            transformed_data = [transform_keys(item) for item in raw_data]
            validated_data = [APIData(**item) for item in transformed_data]
            logger.info(f"Data successfully processed from API: {endpoint}")
            return validated_data
        except Exception as e:
            logger.error(f"Error fetching and processing data: {e}")
            raise

    async def save_data(self, data: List[dict]):
        try:
            logger.info("Saving data to database")
            for item in data:
                self.db_session.add(APIData(**item))
            await self.db_session.commit()
            logger.info("Data successfully saved to database")
        except Exception as e:
            logger.error(f"Error saving data to database: {e}")
            raise

    async def save_to_google_sheets(self, sheet_name: str, data: List[APIData]):
        try:
            logger.info(f"Saving data to Google Sheets: {sheet_name}")
            formatted_data = [[item.id, item.user_id, item.title, item.body] for item in data]
            self.google_sheets_client.append_data(sheet_name, formatted_data)
            logger.info(f"Data successfully saved to Google Sheets: {sheet_name}")
        except Exception as e:
            logger.error(f"Error saving data to Google Sheets: {e}")
            raise
