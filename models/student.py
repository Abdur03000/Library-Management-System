from peewee import Model, IntegerField, CharField
from Database.Config import db

class Student(Model):
    id = IntegerField(primary_key=True)
    name = CharField(null=False)
    email = CharField(null=False)

    class Meta:
        database = db
