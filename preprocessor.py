def preprocess(data):
    pattern=r'\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}\s[ap]m'

    messages=re.split(pattern,data)[1:]

    dates=re.findall(pattern,data)

    cleaned_dates=[entry.replace('\u202f','')for entry in dates]

