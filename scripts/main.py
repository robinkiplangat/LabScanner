import os
from PyPDF2 import PdfReader  
import openai                                                                                                                 
import pdfplumber                                                                                                                              
import ocrspace  
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY') 
ocr_space_api_key = os.getenv('OCR_Space_API') 
                                                                                                                            
                                                                                                                                                
def extract_pdf_text(pdf_path, ocr_space_api_key):                                                                                             
    # Try PyPDF2 first                                                                                                                         
    try:                                                                                                                                       
        pdf = PdfReader(pdf_path)                                                                                                              
        text = ''                                                                                                                              
        for page in pdf.pages:                                                                                                                 
            text += page.extract_text()                                                                                                        
        if text:                                                                                                                               
            return text                                                                                                                        
    except:                                                                                                                                    
        pass                                                                                                                                   
                                                                                                                                                
    # If PyPDF2 fails, try pdfplumber                                                                                                          
    try:                                                                                                                                       
        pdf = pdfplumber.open(pdf_path)                                                                                                        
        text = ''                                                                                                                              
        for page in pdf.pages:                                                                                                                 
            text += page.extract_text()                                                                                                        
        if text:                                                                                                                               
            return text                                                                                                                        
    except:                                                                                                                                    
        pass                                                                                                                                   
                                                                                                                                                
    # If pdfplumber fails, try OCR.space                                                                                                       
    try:                                                                                                                                       
        api = ocrspace.API(apikey=ocr_space_api_key)                                                                                           
        text = api.ocr_file(pdf_path)                                                                                                          
        if text:                                                                                                                               
            return text                                                                                                                        
    except:                                                                                                                                    
        pass                                                                                                                                   
                                                                                                                                                
    # If all methods fail, return an empty string                                                                                              
    return ''

# run main
if __name__ == '__main__':
    pdf_path = 'medReports/NAH_ultrasound.pdf'
    text = extract_pdf_text(pdf_path, ocr_space_api_key)
    print(text)