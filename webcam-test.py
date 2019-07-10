#make sure that bottle is present at that start of the frame
import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

options = {
    'model': 'cfg/tiny-yolo-voc.cfg',
    'load': 'bin/tiny-yolo-voc.weights',
    'threshold': 0.2,
    'gpu': 1.0
}

tfnet=TFNet(options)
#colors is a list of 10 random bgr(rgb) colors 
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
capture=cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
tl=()
bl=()
#countbottle=0
fixed_top_left=()
fixed_bottom_right=()
flag=0
time_flag=0
#elapsed_time=0
while True:
    #start_time=time.time()
    ret, frame=capture.read()
    countbottle=0
    if ret:
        results=tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            #the keys in result dictionary are:
            #[label], [confidence], [topleft][x or y], [bottomright][x or y]
            label=result['label']
            confidence=result['confidence']
            if label=='bottle':
                time_flag=0
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                btl=tl
                bbr=br
                countbottle+=1
                if flag==0:
                    fixed_top_left=tl
                    fixed_bottom_right=br
                    flag+=1
                    print(fixed_top_left, fixed_bottom_right)
                if flag!=0 and (btl[0]>fixed_top_left[0]+20 or btl[0]<fixed_top_left[0]-20 or bbr[1]>fixed_bottom_right[1]+20 or bbr[1]<fixed_bottom_right[1]-20):
                    print("ALARM: bottle has been moved")
        cv2.imshow('frame', frame)
        if countbottle==0:
            if time_flag==0:
                start_time=time.time() # in seconds
                time_flag+=1
            #if time_flag>0:    
            elapsed_time=time.time()

            if elapsed_time-start_time>=10:
                print("ALARM:bottle is not visible for more than 10 seconds")
                time_flag=0
            else:
                frame = cv2.rectangle(frame, btl, bbr, (0,0,255), 5)
                frame = cv2.putText(frame, 'bottle is not visible', btl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('frame', frame)
        
            
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
        
