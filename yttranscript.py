from transformers import pipeline

from youtube_transcript_api import YouTubeTranscriptApi


def summarizer(link):
    VIDEO = link

    #a youtube videos id is need, which is just the part of the url after the "=".
    #for viewing videos on the pc, video id is located after the "=" sign
    #but in mobiles the video id is just after the "/" sign
    if '=' in VIDEO:
        VideoId = VIDEO[(VIDEO.index('=')+1):]
    else:
        #rfind() locates the last occuring element of given character
        VideoId = VIDEO[VIDEO.rfind('/')]

    #getting transcript of video using YoutubeTranscriptApi
    transcript = YouTubeTranscriptApi.get_transcript(VideoId)



    '''
    [{'text': "i'm gonna show you how to become a", 'start': 0.0, 'duration': 3.84}, {'text': 'millionaire all you need', 'start': 0.96, 'duration': 5.52}, {'text': 'is to have one thing that you can get', 'start': 3.84, 'duration': 3.519}, 
    {'text': 'ten dollars for', 'start': 6.48, 'duration': 1.92}, {'text': "i don't care if it's cutting hair", 'start': 7.359, 'duration': 3.28},

    youtube transcripts are displayed like so
    therefore to print only the text, we must only take the values of the dictionary whose key is "text"
    '''

    text = ""

    for i in transcript:
        text += i['text']+' '
    print(text)
    print('---------------------------------------------\n'*5)
    #now text is just the raw transcript text
    #now to summarise

    summarizer = pipeline('summarization')
    #pipeline cannot take giant chunks of text, hence we have to break it down into parts and merge the summarization together:

    split_point = 1000
    Splits = len(text)//split_point #summarize every 500 lines and append to final 
    final_summarized = ""

    final_summarized = []

    for i in range(Splits+1):
        start_point = i*split_point
        end_point = (i+1)*split_point
        line = summarizer(text[start_point:end_point])
        line = line[0]
        line = line['summary_text']
        final_summarized.append(line)

    print(final_summarized)
    return final_summarized

