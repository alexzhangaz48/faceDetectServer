import requests
import cv2

file_data = {'image': open('static/macaw.jpg', 'rb')}


user_info = {'info': 'Lenna'}
 
r = requests.post("http://127.0.0.1:5000/upload", data=user_info, files=file_data)
 
print(r.text)
"""
img = cv2.imread('static/test.jpg')

_, img_encoded = cv2.imencode('.jpg', img)
r = requests.post("http://127.0.0.1:8000", 
    files={'file': img})#_encoded.tostring()})

cv2.imshow('hi there',img)
c = cv2.waitKey(0)
"""

