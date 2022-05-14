import streamlit as st
st.title("これはテストです")
st.write("streamlitは簡単です")

answer = st.button("Hello, world.")

if answer == True:
    st.write("よくできました。")
else:
    st.write("押してください。")

