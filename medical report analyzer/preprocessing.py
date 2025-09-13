import pandas as pd
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import pdf2image
from PIL import Image
from pdf2image import convert_from_path
from nlp_extractor import extract_params
images = convert_from_path(r"F:\ML\Medical\data\medical_himanshini.pdf", dpi=300)
text=[]

for i in range(len(images)):
    text.append(pytesseract.image_to_string(images[i]))

def clean_text(text):
    text = text.replace('\n', ' ')
    text = ' '.join(text.split())
    return text

text_cleaned=[]
for i in range(len(text)):
    text_cleaned.append(clean_text(text[i]))


params=[]
for i in range(len(images)):
    params.append(extract_params(text_cleaned[i]))

