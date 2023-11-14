"""Project settings file"""

import os

from dotenv import load_dotenv

load_dotenv()


class Settings():
    """Class with project settings"""

    DB_HOST_CONNECTION = f"mongodb://{os.getenv('DB_HOST_CONNECTION')}:27017/"
    DB_NAME = os.getenv('DB_NAME')
    DB_COLLECTION_NAME = os.getenv('DB_COLLECTION_NAME')


SETTINGS = Settings()
