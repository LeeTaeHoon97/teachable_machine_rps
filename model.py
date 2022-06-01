from tensorflow.keras.models import load_model
# from PIL import Image, ImageOps
import numpy as np
import cv2
class rpsNet:
    model=None
    def __init__(self):
        #load model
        self.model=load_model('saved_model/keras_model.h5')
    def predict(self,img):
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # image = cv2.resize(img,(224,224))
        
        # cv2.imshow("t",img)
        
        # size = (224, 224)
        # image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(img)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array
        return self.model.predict(data)
        


