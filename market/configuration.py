import os

from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASS = os.getenv('PASS')
DB_NAME = os.getenv('DB_NAME')
HOST = os.getenv('HOST')
# PORT = os.getenv('PORT')
# GITHUB_SECRET_KEY = os.getenv('GITHUB_SECRET_KEY')
# GITHUB_KEY = os.getenv('GITHUB_KEY')
SECRET_DJANGO_KEY = os.getenv('SECRET_KEY')
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
