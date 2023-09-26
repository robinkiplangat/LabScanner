import streamlit as st                                                                                                                         
import pandas as pd                                                                                                                            
from reports_backend import *  # Import all functions from reports_backend.py       
import os                                                                                                                                                                              
import json  
import modal
import time
                                                                                                                                                                                                                                                                                                                                                             
  # Import the backend functions                                                                                                                                                         
# from reports_backend import extract_text_from_pdf, get_report_details, report_summary, lab_summary                                                                                     
                                                                                                                                                                                         
def main():
    # Initialize the Streamlit app                                                                                                                                                         
    st.set_page_config(page_title='Umzima Labs Report Summarizer', layout='wide')                                                                                                          
                                                                                                                                                                                            
    # Create a placeholder for the app content                                                                                                                                             
    content = st.empty()                              
                                                                                                                                                    
    # Set up the title and introductory text for the application                                                                                   
    st.title('Umzima Labs Reports Summarizer')                                                                                                     
    st.write('Welcome to the Umzima Labs Reports Summarizer. Please upload your report below.') 


    uploaded_file = st.file_uploader("Choose a report file", type=['pdf'])

    if uploaded_file is not None:                                                                                                                 
        with st.form('summarize_form'):
            openai_api_key = st.text_input('OpenAI API Key', type = 'password')
            submitted = st.form_submit_button('Submit')
            if submitted and openai_api_key.startswith('sk-'):
                report_details, report_summary = lab_summary(uploaded_file, openai_api_key)
                with st.spinner('Processing...'):
                    time.sleep(3)
                    st.success('Done!')
                    st.write('Report Details:', report_details)
                    st.write('Report Summary:', report_summary)
                del openai_api_key
            else:  
                st.write('Please enter a valid OpenAI API Key.')
            
    else:                                                                                                                                       
        st.write('Please upload a file.')

if __name__ == '__main__':
    main()