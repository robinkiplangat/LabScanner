# LabScanner

LabScanner is a Python application designed to extract and analyze text from lab test reports in PDF format. It extracts text from PDF files using PyPDF2, pdfplumber, and OCR.space, and then analyzes the extracted text to provide a summary with details such as the institution name, date, type of analysis, notes, and results. The results are then outputted in JSON format.

## Installation

To install LabScanner, clone the repository and install the required dependencies:

```
git clone https://github.com/robinkiplangat/LabScanner.git
cd LabScanner
pip install -r requirements.txt
```

## Usage

To use LabScanner, run the following command:

```
streamlit run scripts/reports_frontend.py
```

This will start the Streamlit app, which will allow you to upload a PDF file and get a summary of the report.

### Step-by-Step Explanation of the Code

The code for LabScanner is divided into two main parts: the backend and the frontend. The backend code is responsible for extracting and analyzing the text from the PDF file, while the frontend code is responsible for displaying the results to the user.

The backend code is located in the `scripts/reports_backend.py` file.  The main function in this file is `lab_summary()`, which takes a PDF file as input and returns a summary of the report. 

The `lab_summary()` function first calls the `extract_text_from_pdf()` function to extract the text from the PDF file. It then calls the `get_report_details()` function to get the details of the report, such as the institution name, date, type of analysis, notes, and results. 

Finally, it calls the `generate_summary()` function to generate a summary of the report.

The frontend code is located in the `scripts/reports_frontend.py` file. The main function in this file is `main()`, which starts the Streamlit app. The `main()` function first sets up the title and introductory text for the app. 

It then creates a form that allows the user to upload a PDF file. When the user submits the form, the `main()` function calls the `lab_summary()` function to get a summary of the report. It then displays the summary to the user.

## Conclusion

LabScanner is a powerful tool that can be used to extract and analyze text from lab test reports.

Happy to add other features that we can update on, create a PR and lets collaborate
