import glob
import os

import cv2
import numpy as np

#detects face from latest snap in the directory
files_path = os.path.join('F:\yolo\smart-survelliance\screenshots', '*.png')
files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True) 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for i in files:
        #print(i)
        j = 1
        img = cv2.imread(str(i))
        grayImg = cv2.cvtColor(img, 0)
        faces = face_cascade.detectMultiScale(grayImg, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 2)
        filename = str(j) + 'Face.png'
        #path = 'F:\yolo\smart-survelliance\face-detected'
        cv2.imwrite(i, img)
        #print(i)
        #cv2.imwrite(filename, img)
        j += 1
"""
i = 1
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread(str(files[0]))
grayImg = cv2.cvtColor(img, 0)
faces = face_cascade.detectMultiScale(grayImg, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 2)
filename = str(i) + 'Face.png'
cv2.imwrite(filename, img)
i += 1
if cv2.waitKey(1) & 0xff == ord('q'):
    cv2.destroyAllWindows()

"""

"""
#detects face from all snaps in the dir
for i in os.listdir('F:\yolo\smart-survelliance\screenshots'):
        j = 1
        print(i)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        img = cv2.imread(i)
        grayImg = cv2.cvtColor(img, 0)
        faces = face_cascade.detectMultiScale(grayImg, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 2)
        filename = str(j) + 'Face.png'
        path = 'F:\yolo\smart-survelliance\face-detected'
        cv2.imwrite(os.path.join(path, filename), img)
        j += 1
        if cv2.waitKey(1) & 0xff == ord('q'):
            cv2.destroyAllWindows()
"""
	
