import os
from PyPDF2 import PdfReader
from languagetools import summarizer
import openai
import pdfplumber
import ocrspace
import json
import modal
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OpenAI_API_KEY')
ocr_space_api_key = os.getenv('OCR_Space_API')


stub = modal.Stub("umzima_labs")
stub = modal.Stub(image=modal.Image.debian_slim().pip_install("openai",
                                                            "languagetools==0.0.3",
                                                            "ocrspace==2.3.0",
                                                            "pdfplumber==0.10.2",
                                                            "PyPDF2==3.0.1",
                                                            "python-dotenv==1.0.0",
                                                            ))



@stub.function(secret=modal.Secret.from_name("ocr_space_api_key"))
def extract_text_from_pdf(file_obj):
    print ("Starting Report Details Extraction Function")
    print ("Local Path:", file_obj)

    # Perform the Extraction
    # Try PyPDF2 first
    try:
        pdf = PdfReader(file_obj)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        if text:
            return text
    except:
        pass

    # If PyPDF2 fails, try pdfplumber
    try:
        pdf = pdfplumber.open(file_obj)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        if text:
            return text
    except:
        pass

    # If pdfplumber fails, try OCR.space
    try:
        api = ocrspace.API(apikey=os.environ["OCR_Space_API"])
        text = api.ocr_file(file_obj)
        if text:
            return text
    except:
        pass

    # If all methods fail, return an empty string
    return ''


def save_text_on_doc(text):
    with open('data/lab_report.txt', 'w') as file:
        file.write(text)

# Extract the details from the of the Lab Report

@stub.function(secret=modal.Secret.from_name("openai.api_key"))
def get_report_details(text):
    import openai
    instructPrompt = """ You will be provided with text extracted from a Lab Report.
    Write a concise and summary that captures the key points and return the output info as a json object
    Please ensure You have understood the context and extract the key details extracted from the lab test report.
    Provide a summary with the following details:
    - Instituiton name,
    - Date,
    - Type of analysis,
    - Notes
    - Results

    """

    request = instructPrompt + text

    chatOutput = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                            {"role": "user", "content": request}
                                                            ]
                                                )

    labReportInfo = chatOutput.choices[0].message.content

    return labReportInfo


# Create a summary of the report
@stub.function(secret=modal.Secret.from_name("openai.api_key"))
def report_summary(text):
    OpenAI_API_KEY = openai.api_key
    labReportSummary = summarizer.summarize(text)

    return labReportSummary

@stub.function(secret=modal.Secret.from_name("openai.api_key"))
def lab_summary(file_obj):
    openai.api_key = os.getenv('OpenAI_API_KEY')
    OPENAI_API_KEY = openai.api_key
    text = extract_text_from_pdf(file_obj)
    repo_info = get_report_details(text)
    repo_summary = report_summary(text)

    return repo_info, repo_summary

# @stub.local_entrypoint()
# def main(file_obj):
#   output = lab_summary(file_obj)
#   return output
