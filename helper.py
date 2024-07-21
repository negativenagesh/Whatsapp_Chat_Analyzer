from urlextract import URLExtract
extract=URLExtract()
import nltk
from wordcloud import WordCloud
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import pandas as pd
from collections import Counter



def fetch_stats(selected_user,df):

    if selected_user!="Overall":
        df=df[df['user']==selected_user]

    num_messages = df.shape[0]
    words=[]
    for message in df['messages']: 
        words.extend(message.split())

    numberofmediamsgs=df[df['messages']=='<Media omitted>\n'].shape[0]

    links=[]
    for message in df['messages']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),numberofmediamsgs,len(links)


def most_busy_users(df):
    mostbusyusers=df['user'].value_counts().head(30)
    df=(round((df['user'].value_counts()/df.shape[0])*100,2)).reset_index().rename(columns={'user':'Name','count':'Percentage of contribution'})
    
    return mostbusyusers,df


def create_wordcloud(selected_user,df):

    if selected_user!="Overall":
        df=df[df['user']==selected_user]
    
    wc=WordCloud(width=500,min_font_size=10)
    df_wc=wc.generate(df['messages'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):

    if selected_user!="Overall":
        df=df[df['user']==selected_user]
    
    temp=df[df['user']!='group_notification']
    temp=temp[temp['messages']!='<Media omitted>\n']

    words=[]

    for message in temp['messages']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_df