import streamlit as st
import preprocessor

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file=st.sidebar.file_uploader("Upload a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)


    st.dataframe(df)

    user_list=df['user'].unique().tolist()

    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0,"Overall")

    st.sidebar.selectbox("Show analysis with respect to",user_list)

    if st.sidebar.button("Show analysis"):
        
        col1,col2,col3,col4=st.columns(4)

        with col1:
            st.header("Total Messages")