# load environment variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TICKETMASTER_API_KEY = os.getenv('TICKETMASTER_API_KEY')
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

    DB_PATH = os.getenv('DB_PATH', 'data/concerts.db')

    GENRE = 'metal' # maybe add rock
    COUNTRY_CODE = 'US'
    STATE_FILTERS = ['DC', 'MD', 'VA']
    LOOKAHEAD_DAYS = 90

    @classmethod
    def validate(cls):
        required = [
            cls.TICKETMASTER_API_KEY,
            cls.EMAIL_ADDRESS,
            cls.EMAIL_PASSWORD
        ]
        if not all(required):
            raise ValueError("Missing required environment variables")