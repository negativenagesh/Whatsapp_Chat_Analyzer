from urlextract import URLExtract
extract=URLExtract()
from wordcloud import wordcloud

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
    
    wc=wordcloud(width=500,min_font_size=10)
    df_wc=wc.generate(df['messages'].str.cat(sep=" "))
    return df_wc