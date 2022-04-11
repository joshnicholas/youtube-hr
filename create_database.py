from peewee import *

db = SqliteDatabase('responses.db')

class Response(Model):

    firstName = CharField()
    lastName = CharField()

    postcode = CharField()
    lift12kgs = BooleanField()
    license = BooleanField()

    email = CharField()
    link = CharField()

    time = DateTimeField()

    transcript = TextField()
    prediction = CharField()

    class Meta:
        database = db

db.connect()

db.create_tables([Response])