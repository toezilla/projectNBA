## Defining a base model that Points at the database object we want to use

from peewee import *
from settings import Settings

settings = Settings()

class BaseModel(Model):
    class Meta:
        database = settings.db
