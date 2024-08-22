import streamlit as st 
import spacy 
from spacy import displacy 
nlp=spacy.load("en_core_web_sm") #this the model

# funcation to extract named entity recognation 

def extract(text):
    doc=nlp(text)
    entities=[(ent.text,ent.label_) for ent in doc.ents]
    return entities

def show_ner(doc):
    html=displacy.render(doc,style="ent",jupyter=False)
    return html

st.title("text extraction with NER")
st.write("enter text like names dates others ")

text=st.text_area("please enter text here ")

if text:
    doc=nlp(text)
    entities=extract(text)
    st.subheader("extrected entes")
    st.write(entities)

    st.markdown(show_ner(doc),unsafe_allow_html=True)