#pip install pytesseract
import pytesseract
#pip install pillow
from PIL import Image

# install tesseract-ocr for windows
#provide location of the installed application
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open('# path to image')
text = pytesseract.image_to_string(img)
with open('result_text','w') as f:
    f.write(text)

