# %%
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import time

# %%

# vid = YouTubeTranscriptApi.get_transcript('gyFaBZ_BQhc')

# print(vid)

# [{'text': 'hello my name is praveen Yewon and I', 'start': 0.0, 'duration': 3.78},
# {'text': 'would like to apply as one of your', 'start': 2.49, 'duration': 3.84}, 
# {'text': "accounting associates I'm 22 years old", 'start': 3.78, 'duration': 4.739},
# {'text': "I've earned my degree in Bachelor of", 'start': 6.33, 'duration': 3.72}, 
# {'text': 'Science and accountancy in the', 'start': 8.519, 'duration': 4.111},
# {'text': 'University of Santo Tomas and recently', 'start': 10.05, 'duration': 5.27}, 
# {'text': 'passed the CPA Board Exam last October', 'start': 12.63, 'duration': 5.1}, 
# {'text': 'hiring me is like getting an all-in-one', 'start': 15.32, 'duration': 5.08}, 
# {'text': 'package I could do not only financial', 'start': 17.73, 'duration': 5.16}, 
# {'text': 'statements but also tasks in other areas', 'start': 20.4, 'duration': 5.219}, 
# {'text': 'such as management marketing are even', 'start': 22.89, 'duration': 5.52}, 
# {'text': 'graphics design I consider myself as a', 'start': 25.619, 'duration': 4.65},
# {'text': 'team player but could do jobs', 'start': 28.41, 'duration': 5.309}, 
# {'text': "excellently alone I'm resilient and can", 'start': 30.269, 'duration': 6.961},
# {'text': "handle stress easily so if you're", 'start': 33.719, 'duration': 5.971}, 
# {'text': 'interested in hiring me please call me', 'start': 37.23, 'duration': 5.099}, 
# {'text': "or send me a message and together we'll", 'start': 39.69, 'duration': 5.209}, 
# {'text': 'get things done', 'start': 42.329, 'duration': 2.57},
# {'text': '[Music]', 'start': 47.12, 'duration': 3.09}, {'text': '[Music]', 'start': 52.46, 'duration': 3.65}, 
# {'text': 'you', 'start': 54.05, 'duration': 2.06}]

# %%

df = pd.read_csv('data/videolist_playlist11_2022_03_21-10_22_18.tab', delimiter='\t')

# ids = df['videoId'].unique().tolist()

df.dropna(subset=['videoId'], inplace=True)

# df = df[:5]

for index, row in df.iterrows():
    try:
        vid = row['videoId']
        channel = row['channelTitle'].lower().replace("\s", '')
        print(channel)

        response = YouTubeTranscriptApi.get_transcript(vid)

        stringo = ''

        for thing in response:
            stringo += thing['text']
            stringo += ' '

        print(stringo)

        with open(f'data/scraped/{channel}.txt', 'w') as f:
            f.write(stringo)

    except Exception as e:
        print(e)
        continue
    time.sleep(1)

# p = df

# print(p)
# print(p.columns)



# %%
