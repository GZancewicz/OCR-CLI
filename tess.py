
import sys
import cv2
import pytesseract
import urllib.request
import numpy as np

url_response = urllib.request.urlopen(sys.argv[1])
img = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)

text = pytesseract.image_to_string(img)
print(text)
sys.stdout.flush()
