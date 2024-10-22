import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

def get_filename(file):
    name = file.name.rsplit(".", 1)[0]  # Split at the last dot and take the first part
    return name

uploaded_file=st.sidebar.file_uploader("Upload a file")
if uploaded_file is not None:
    filename = get_filename(uploaded_file)
    st.write(f"## {filename}")
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)

    user_list=df['user'].unique().tolist()

    if "group_notification" in user_list:
        user_list.remove("group_notification")

    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user=st.sidebar.selectbox("Show analysis with respect to",user_list)

    if st.sidebar.button("Show analysis"):
        num_messages,words,numberofmediamsgs,num_links=helper.fetch_stats(selected_user,df)
        
        st.title("Top Statistics")
        col1,col2,col3,col4=st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header('Total Words')
            st.title(words)

        with col3:
            st.header("Total Media Shared")
            st.title(numberofmediamsgs)

        with col4:
            st.header("Links shared in this group")
            st.title(num_links)

        st.title('Record of number of messages monthwise')

        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        fig, ax = plt.subplots(figsize=(20, 6))

        ax.plot(timeline['time'],timeline['messages'],color='green')
        plt.xticks(rotation="vertical")
        st.pyplot(fig)
        
        st.title('Record of number of messages Daywise')

        daily_timeline=helper.daily_timeline(selected_user,df)
        fig,ax=plt.subplots()
        fig, ax = plt.subplots(figsize=(20, 6))

        ax.plot(daily_timeline['only_date'],daily_timeline['messages'],color='black')
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        st.title('Activity Map')
        col1,col2=st.columns(2)

        with col1:
            st.header("Most busy Day")
            busy_day=helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy Month")
            busy_month=helper.month_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title('Weekly activity Map')
        user_heatmap=helper.activity_heatmap(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(user_heatmap)
        st.pyplot(fig)

        if selected_user == "Overall":
            st.title('Most busy users')
            mostbusyusers,new_df=helper.most_busy_users(df)
            fig, ax =plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                bars=ax.bar(mostbusyusers.index,mostbusyusers.values)

                plt.xticks(rotation='vertical')

                #adding annotations for each bar
                ax.bar_label(bars, padding=3)

                plt.tight_layout()
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)
            
        st.title('Wordcloud for most repeated words in this chat')
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        st.title('Most common words ranking')
        most_common_df=helper.most_common_words(selected_user,df)

        fig,ax=plt.subplots()

        ax.bar(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        emojidf=helper.emoji_helper(selected_user,df)
        st.title("Emoji Analysis")

        col1,col2=st.columns(2)

        with col1:
            st.dataframe(emojidf)

        with col2:
            fig,ax=plt.subplots()
            ax.pie(emojidf['Count'].head(),labels=emojidf['Emoji'].head(),autopct="%0.2f")
            st.pyplot(fig)