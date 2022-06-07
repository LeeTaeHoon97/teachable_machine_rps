import sys
import cv2
import numpy as np
import base64

def readb64(encoded_data):
   nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
   img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   cv2.imshow(img)
   return img

def add(base64_img):
    print(base64_img)
    res=readb64(base64_img)
    return res
    # return result

add(str(sys.argv[1]))