from PIL import ImageGrab
import pytesseract
import clipboard

pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img = ImageGrab.grabclipboard()
text = pytesseract.image_to_string(img)
print("\n" , text)
clipboard.copy(text)

    

