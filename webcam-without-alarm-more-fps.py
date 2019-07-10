"""import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import winsound
import pyscreenshot as ImageGrab

options = {
    'model': 'cfg/tiny-yolo-voc.cfg',
    'load': 'bin/tiny-yolo-voc.weights',
    'threshold': 0.2,
    'gpu': 1.0
}


tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
countbottle = 0
tl = ()
br = ()
imgcounter = 0
screenshotflag = 0
while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            #print(tl, 'topleft')
            
            label = result['label']
            confidence = result['confidence']
            #print(label)
            if label == 'bottle':
                pass
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(
                    frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            #if(label == 'bottle'):
                btl = tl
                bbr = br
                countbottle += 1
        cv2.imshow('frame', frame)
        if countbottle == 0:
            if screenshotflag == 0:
                im = ImageGrab.grab()
                st = str(imgcounter)+'screenshot.png'
                im.save('F:\yolo\smart-survelliance\screenshots\\'+st)
                imgcounter += 1
                screenshotflag = 1
            frame = cv2.rectangle(frame, btl, bbr, (0,0,255), 5)
            frame = cv2.putText(
                    frame, 'bottle is missing', btl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('frame', frame)
        #print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        else:
           screenshotflag = 0
           winsound.PlaySound(None, winsound.SND_ASYNC)
        countbottle = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #winsound.PlaySound(None, winsound.SND_ASYNC)
        break

capture.release()
cv2.destroyAllWindows()
"""

import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import winsound
import pyscreenshot as ImageGrab
import os

options = {
    'model': 'cfg/tiny-yolo-voc.cfg',
    'load': 'bin/tiny-yolo-voc.weights',
    'threshold': 0.2,
    'gpu': 1.0
}


tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
countbottle = 0
tl = ()
br = ()
##########
imgcounter = 0
screenshotflag = 0
cordscount = 0
while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            #print(tl, 'topleft')
            
            label = result['label']
            confidence = result['confidence']
            #print(label)
            
            if label == 'bottle':
                
                if cordscount == 0:
                    cordstl = tl
                    cordsbr = br
                    cordscount = 1

                    
                text = 'bottle'#'{}: {:.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(
                    frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            #if(label == 'bottle'):
                btl = tl
                bbr = br
                countbottle += 1
        cv2.imshow('frame', frame)
        ###############
        if abs(cordstl[0]-btl[0]) > 35 or abs(cordstl[1]-btl[1]) > 35 or abs(cordsbr[0]-bbr[0]) > 35 or abs(cordsbr[1]-bbr[1]) > 35:
            if screenshotflag == 0:
                im = ImageGrab.grab()
                st = str(imgcounter)+'misplaced.png'
                im.save(os.getcwd()+'\screenshots\\'+st)
                imgcounter += 1
                screenshotflag = 1
            frameMiss = cv2.rectangle(frame, btl, bbr, (0,255,0), 5)
            frameMiss = cv2.putText(
                    frame, 'bottle misplaced', btl, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
            cv2.imshow('frame', frameMiss)
            
        ###############
        if countbottle == 0:
            if screenshotflag == 0:
                im = ImageGrab.grab()
                st = str(imgcounter)+'missing.png'
                im.save(os.getcwd()+'\screenshots\\'+st)
                imgcounter += 1
                screenshotflag = 1
            frame = cv2.rectangle(frame, btl, bbr, (0,0,255), 5)
            frame = cv2.putText(
                    frame, 'bottle is missing', btl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('frame', frame)
        #print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        else:
            screenshotflag = 0
         #  winsound.PlaySound(None, winsound.SND_ASYNC)
        countbottle = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #winsound.PlaySound(None, winsound.SND_ASYNC)
        break

capture.release()
cv2.destroyAllWindows()

import faceDetectionFromScreenshot


