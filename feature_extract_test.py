import pandas as pd
import re 

import spacy

NER = spacy.load("en_core_web_lg", 
disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

# print(spacy.explain('NORP'))

df = pd.read_csv('data/mit_dataset/interview_transcripts_by_turkers.csv', names=['Type', 'Transcript'])
# 'Type', 'Transcript'

## Grab only the pre interviews:

df = df.loc[~df['Type'].str.contains("pp")]

## Split transcript to remove interviewer

# df['Transcript'] = df['Transcript'].str.split("|")

# df = df[:1]

keep_ents = ['NORP','ORG', 'EVENT','PERSON','FAC','PRODUCT','WORK_OF_ART']

big_stringo = ' '

for index, row in df.iterrows():
    print(index)
    transcript = row['Transcript']
    transcript = transcript.split("|")
    transcript = [x for x in transcript if "Interviewer" not in x]

    activities = [x for x in transcript if "activities" in x.lower()]
    interests = [x for x in transcript if "interest" in x.lower()]

    interviewee = " ".join(transcript)
    interviewee = interviewee.replace('Interviewee:', '')

    proc = NER(interviewee)

    extra = [x.text for x in proc.ents if x.label_ in keep_ents]

    extra = list(set(extra))

    print(extra)

    # big_stringo += interviewee

# proc = NER(big_stringo)

# refs =  [x.label_ for x in proc.ents]
# refs = list(set(refs))
# refs = [(x, spacy.explain(x)) for x in refs]

# # reffers = 



# print(refs)





    # print(interests)

    # print(activities)
    # print(interviewee)

    # print(transcript)
    # print(row['Transcript'])

# p = df 

# print(p['Transcript'])
# print(p.columns)



