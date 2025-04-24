from datetime import date, datetime
from peewee import Model, IntegerField, ForeignKeyField, DateField
from Database.Config import db
from models.student import Student
from models.book import Book

class Order(Model):
    id            = IntegerField(primary_key=True)
    student       = ForeignKeyField(Student, backref='orders')
    book          = ForeignKeyField(Book, backref='orders')
    rent_per_day  = IntegerField()
    rented_date   = DateField()
    return_date   = DateField(null=True)
    total_days    = IntegerField(default=0)
    total_rent    = IntegerField(default=0)

    class Meta:
        database = db
    