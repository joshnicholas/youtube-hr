from flask import Flask,render_template,request
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

# db.create_tables([Response])

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


    responser = YouTubeTranscriptApi.get_transcript(vid)

    stringo = ''

    for thing in responser:
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

app = Flask(__name__)

@app.route('/hr')
def form():
    return render_template('form.html')
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form.to_dict()
        form_data['Transcript'] = get_transcript(form_data["Youtube"])
        processo(form_data)
        print("\n\n\n\n\n\n\n")
        print(type(form_data))
        print("\n\n\n\n\n\n\n")
        return render_template('return.html',form_data = form_data)
