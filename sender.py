from youtube_transcript_api import YouTubeTranscriptApi
from peewee import *
import datetime
import pytz

when = datetime.datetime.now().astimezone(pytz.timezone("Australia/Brisbane"))

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

objecto = {"FirstName": "Jawsh",
            "FastName": "Something",
            "Postcode": 2342,
            "Lift12kgs": True,
            "License": False,
            "Email": "hi@something",
            "Youtube": 'https://www.youtube.com/watch?v=LspIeUElIFA',
            "Prediction": 1
            }


def get_transcript(urlo):

    vid = urlo.split("=")[-1]


    response = YouTubeTranscriptApi.get_transcript(vid)

    stringo = ''

    for thing in response:
        stringo += thing['text']
        stringo += ' '

    # print(stringo)
    return stringo

def processo(obj):
    # obj['Transcript'] = get_transcript(obj["Youtube"])
    Response.create(
    firstName = objecto['FirstName'],
    lastName = objecto['FastName'],

    postcode = objecto['Postcode'],
    lift12kgs = objecto['Lift12kgs'],
    license = objecto['License'],

    email = objecto['Email'],

    time = when,

    link = objecto['Youtube'],
    transcript = get_transcript(objecto['Youtube']),
    # transcript = "Hi",
    prediction = objecto['Prediction'])

print(when)

processo(objecto)

# response = YouTubeTranscriptApi.get_transcript('https://www.youtube.com/watch?v=LspIeUElIFA')

# print(response)