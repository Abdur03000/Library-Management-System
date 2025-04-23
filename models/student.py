from peewee import Model, IntegerField, CharField
from Database.Config import db

class Student(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    email = CharField()

    class Meta:
        database = db
