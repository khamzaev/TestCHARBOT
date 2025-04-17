from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from injectable import injectable

from app import logger


@injectable
class GoogleSheetsClient:
    def __init__(self, credentials_file: str, spreadsheet_id: str):
        """
        Инициализация клиента Google Sheets API.
        :param credentials_file: Путь к файлу учетных данных.
        :param spreadsheet_id: ID таблицы Google Sheets.
        """
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.credentials = Credentials.from_service_account_file(
            self.credentials_file,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        self.service = build("sheets", "v4", credentials=self.credentials)

    def append_data(self, sheet_name: str, data: list):
        try:
            logger.info(f"Appending data to Google Sheets: {sheet_name}")
            body = {"values": data}
            self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=sheet_name,
                valueInputOption="RAW",
                body=body
            ).execute()
            logger.info(f"Data successfully appended to Google Sheets: {sheet_name}")
        except Exception as e:
            logger.error(f"Error appending data to Google Sheets: {e}")
            raise
