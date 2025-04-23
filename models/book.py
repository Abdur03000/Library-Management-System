from peewee import Model, IntegerField, CharField
from Database.Config import db

class Book(Model):
    id = IntegerField(primary_key=True)
    title = CharField()
    author = CharField()

    class Meta:
        database = db

