import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")

def get_filename(file):
  return file.name.rsplit(".", 1)[0]


uploaded_file=st.sidebar.file_uploader("Upload a file")
if uploaded_file is not None:
    filename = get_filename(uploaded_file)
    st.write(f"## {filename}")
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)


    st.dataframe(df)

    user_list=df['user'].unique().tolist()

    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user=st.sidebar.selectbox("Show analysis with respect to",user_list)

    if st.sidebar.button("Show analysis"):
        num_messages,words,numberofmediamsgs,num_links=helper.fetch_stats(selected_user,df)
        
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
            
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)