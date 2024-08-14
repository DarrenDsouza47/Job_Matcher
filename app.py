import streamlit as st
import requests
import json
from pdf_utils import extract_text_pdf
from parser import resume_parser

FLASK_URL = 'http://127.0.0.1:5000/match'


def get_matches(parsed_resume):
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'resume': parsed_resume})
    response = requests.post(FLASK_URL, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['matches']
    else:
        st.error(f"Error: {response.status_code}")
        return []

st.title('Job Matching System')

pdf_file = st.file_uploader("Upload resume:",type='pdf')

parsed_resume_text={}
if pdf_file:
    resume_text=extract_text_pdf(pdf_file)

    parsed_resume_text=resume_parser(resume_text)

if parsed_resume_text:
    st.subheader("Parsed Resume Content")
    st.write(parsed_resume_text)

if st.button('Get Job Matches'):
    if parsed_resume_text:
        with st.spinner('Getting matches...'):
            matches = get_matches(parsed_resume_text)
            if matches:
                st.write("Top 3 Job Matches:")
                for match in matches:
                    st.write(match)
                    st.write("---")
            else:
                st.write("No matches found.")
    else:
        st.warning("Please enter some resume text.")

