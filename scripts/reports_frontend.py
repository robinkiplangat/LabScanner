import streamlit as st                                                                                                                         
import pandas as pd                                                                                                                            
from reports_backend import *  # Import all functions from reports_backend.py       
import os                                                                                                                                                                              
import json  
import modal
                                                                                                                                                                                                                                                                                                                                                             
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

    # Create a button that will process the uploaded file when clicked                                                                              
    if st.button('Process Report'):                                                                                                                 
        if uploaded_file is not None:
            # Call the lab_summary function with the uploaded file as the argument
        
            report_details, report_summary = lab_summary(uploaded_file)
                                                                        
                                                                                                                                                
            # Display the report details and the summary                                                                                            
            st.write('Report Details:', report_details)                                                                                             
            st.write('Report Summary:', report_summary)                                                                                             
        else:                                                                                                                                       
            st.write('Please upload a file.')
            
    def process_report_info(pdf_path):
        f = modal.Function.lookup("umzima_labs","lab_summary")
        output = f.remote()
        return output

if __name__ == '__main__':
    main()
