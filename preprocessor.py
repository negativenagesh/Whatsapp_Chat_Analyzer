import re
import pandas as pd

def preprocess(data):
    pattern='\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}\s[ap]m'

    messages=re.split(pattern,data)[1:]

    dates=re.findall(pattern,data)

    cleaned_dates=[entry.replace('\u202f','')for entry in dates]

    df=pd.DataFrame({'user_message':messages,'message_date':cleaned_dates})

    df['message_date'] = pd.to_datetime(df['message_date'],format='%d/%m/%y, %I:%M%p')
    
    df.rename(columns={'message-date':'date'},inplace=True)

    users=[]
    messages=[]
    for message in df['user_message']:
        entry=re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user']=users
    df['messages']=messages
    df.drop(columns=['user_message'],inplace=True)

    df['year']=df['message_date'].dt.year
    df['month_num']=df['message_date'].dt.month
    df['month']=df['message_date'].dt.month_name()
    df['weekday'] = df['message_date'].dt.day_name()
    df['date'] = df['message_date'].dt.day
    df['only_date']=df['message_date'].dt.date
    df['day_name']=df['message_date'].dt.day_name()
    df['day_of_month']=df['message_date'].dt.day
    df['hour']=df['message_date'].dt.hour
    df['minute']=df['message_date'].dt.minute

    return df