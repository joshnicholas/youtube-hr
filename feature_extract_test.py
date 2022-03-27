import pandas as pd
import re 


df = pd.read_csv('data/mit_dataset/interview_transcripts_by_turkers.csv', names=['Type', 'Transcript'])
# 'Type', 'Transcript'

## Grab only the pre interviews:

df = df.loc[~df['Type'].str.contains("pp")]

## Split transcript to remove interviewer

# df['Transcript'] = df['Transcript'].str.split("|")

df = df[:1]

for index, row in df.iterrows():
    transcript = row['Transcript']
    transcript = transcript.split("|")
    transcript = [x for x in transcript if "Interviewer" not in x]

    activities = [x for x in transcript if "activities" in x.lower()]
    interests = [x for x in transcript if "interest" in x.lower()]

    interviewee = " ".join(transcript)
    interviewee = interviewee.replace('Interviewee:', '')

    print(interests)

    # print(activities)
    # print(interviewee)

    # print(transcript)
    # print(row['Transcript'])

# p = df 

# print(p['Transcript'])
# print(p.columns)



