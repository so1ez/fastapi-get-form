"""Project settings file"""

import os

from dotenv import load_dotenv

load_dotenv()


class Settings():
    """Class with project settings"""

    DB_CONNECTION: str = os.getenv('DB_CONNECTION')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_COLLECTION_NAME: str = os.getenv('DB_COLLECTION_NAME')


SETTINGS = Settings()
