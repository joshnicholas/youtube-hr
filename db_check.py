import pandas as pd
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

for story in Response.select().where(Response.license == False):
    print(story.transcript)