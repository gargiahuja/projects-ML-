import pytesseract
from PIL import Image
import pdfplumber
import tempfile
import fitz  # PyMuPDF
import os

def extract_text(path):
    full_text = ""

    try:
        # Try using pdfplumber first
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and text.strip():
                    full_text += f"\n\n--- Page {i+1} ---\n{text}"
        
        # If no text was found (image-based PDF), do OCR
        if not full_text.strip():
            full_text = ocr_pdf_with_tesseract(path)

    except Exception as e:
        print("PDF processing failed, falling back to OCR:", e)
        full_text = ocr_pdf_with_tesseract(path)

    return full_text

def ocr_pdf_with_tesseract(pdf_path):
    """OCR each page using pytesseract after converting to image"""
    doc = fitz.open(pdf_path)  # PyMuPDF
    ocr_text = ""
    
    for i in range(len(doc)):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=300)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            pix.save(tmp.name)
            img = Image.open(tmp.name)
            text = pytesseract.image_to_string(img)
            ocr_text += f"\n\n--- OCR Page {i+1} ---\n{text}"
            os.remove(tmp.name)

    return ocr_text
