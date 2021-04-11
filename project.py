import wikipediaapi as wiki
import streamlit as st
import spacy
pageName=st.text_input("Enter Query")
nlp=spacy.load("en_core_web_sm")
if(st.button("GO!!")):
    if(pageName!=""):
        data=nlp(wiki.Wikipedia('en').page(pageName).summary)
        html=spacy.displacy.render(data,style="ent")
        st.write(html,unsafe_allow_html=True)