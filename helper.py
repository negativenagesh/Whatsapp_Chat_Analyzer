def fetch_stats(selected_user,df):

    if selected_user!="Overall":
        df=df[df['user']==selected_user]

    num_messages = df.shape[0]
    words=[]
    for message in df['messages']: 
        words.extend(message.split())

    numberofmediamsgs=df[df['messages']=='<Media omitted>\n'].shape[0]

    return num_messages,len(words),numberofmediamsgs