# import os
# os.system('ls')
# os.system('tesseract testimg.png stdout')

import sys
import cv2
import pytesseract
import urllib.request
import numpy as np

#testurl = "https://tinyurl.com/wkr9fm6u"

#img = cv2.imread("testimg.png")

# https://stackoverflow.com/a/65743253/4038302
#url_response = urllib.request.urlopen(testurl)
url_response = urllib.request.urlopen(argv[1])
img = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)

text = pytesseract.image_to_string(img)
print(text)
sys.stdout.flush()

#