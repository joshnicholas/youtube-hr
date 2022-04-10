from youtube_transcript_api import YouTubeTranscriptApi
from peewee import *
import datetime
import pytz

when = datetime.datetime.now().astimezone(pytz.timezone("Australia/Brisbane"))

db = SqliteDatabase('databases/responses.db')

class response(Model):

    firstName = CharField()
    lastName = CharField()

    postcode = CharField()
    lift12kgs = BooleanField()
    license = BooleanField()

    email = CharField()
    youtube = CharField()

    time = DateTimeField

    management = TextField()
    transcript = TextField()
    prediction = CharField()

    class Meta:
        database = db

db.connect()

objecto = {"firstName": "Jawsh",
            "lastName": "Something",
            "postcode": 2342,
            "lift12kgs": True,
            "license": False,
            "Email": "hi@something",
            "Youtube": 'https://www.youtube.com/watch?v=Nv6mDeFPT2M'
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
    obj['Transcript'] = get_transcript(obj["Youtube"])
    response.create(site = objecto["website"], 
        party = objecto['party'],
        division = objecto['division'],
        candidate_type = objecto['type'],
        title = objecto['headline'],
        url= objecto['url'], 
        name = nammo,
        cleaned_name = cleaned_nammo,
        published_datetime= date_fixer(objecto['date']),
        processed = False,
        scraped_datetime = date_fixer(today), 
        body= objecto['body'])
