from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import time

'https://www.youtube.com/watch?v=Nv6mDeFPT2M'

def get_transcript(urlo):

    vid = urlo.split("=")[-1]


    response = YouTubeTranscriptApi.get_transcript(vid)

    stringo = ''

    for thing in response:
        stringo += thing['text']
        stringo += ' '

    # print(stringo)
    return stringo 

get_transcript('https://www.youtube.com/watch?v=Nv6mDeFPT2M')