import os
from dotenv import load_dotenv
from peewee import *

load_dotenv()

## Initializing a Database

DB_NAME = 'nba_stats'
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'eddy2080'
'''
db = MySQLDatabase(
    DB_NAME,
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    charset='utf8mb4')


DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

'''
class Settings:
    def __init__(self):
        self.db = MySQLDatabase(
            DB_NAME,
            host = DB_HOST,
            user = DB_USER,
            password=DB_PASSWORD,
            charset='utf8mb4'
        )
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"

