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
capture_1=cv2.VideoCapture(0)
capture_2=cv2.VideoCapture("")
# 0 for webcam

capture_1.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
capture_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

capture_2.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
capture_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)


#for feed1
tl=()
bl=()
fixed_top_left=()
fixed_bottom_right=()
flag=0
time_flag=0

#for feed2
tl2=()
bl2=()
fixed_top_left2=()
fixed_bottom_right2=()
flag2=0
time_flag2=0


while True:
    #start_time=time.time()
    ret1, frame1=capture_1.read()
    ret2, frame2=capture_2.read()
    countbottle1=0
    countbottle2=0
    if ret1 and ret2:
        results1=tfnet.return_predict(frame1)
        results2=tfnet.return_predict(frame2)
        for color, result in zip(colors, results1):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            #the keys in result dictionary are:
            #[label], [confidence], [topleft][x or y], [bottomright][x or y]
            label=result['label']
            confidence=result['confidence']
            if label=='bottle':
                time_flag=0
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame1 = cv2.rectangle(frame1, tl, br, color, 5)
                frame1 = cv2.putText(frame1, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                btl_1=tl
                bbr_1=br
                countbottle1+=1
                if flag==0:
                    fixed_top_left=tl
                    fixed_bottom_right=br
                    flag+=1
                    print(fixed_top_left, fixed_bottom_right)
                if flag!=0 and (btl_1[0]>fixed_top_left[0]+50 or btl_1[0]<fixed_top_left[0]-50 or bbr_1[1]>fixed_bottom_right[1]+50 or bbr_1[1]<fixed_bottom_right[1]-50):
                    pass #print('bottle has been moved')    
        for color, result in zip(colors, results2):
            tl2 = (result['topleft']['x'], result['topleft']['y'])
            br2 = (result['bottomright']['x'], result['bottomright']['y'])
            #the keys in result dictionary are:
            #[label], [confidence], [topleft][x or y], [bottomright][x or y]
            label=result['label']
            confidence=result['confidence']
            if label=='bottle':
                time_flag2=0
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame2 = cv2.rectangle(frame2, tl2, br2, color, 5)
                frame2 = cv2.putText(frame2, text, tl2, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                btl_2=tl2
                bbr_2=br2
                countbottle2+=1
                if flag2==0:
                    fixed_top_left2=tl2
                    fixed_bottom_right2=br2
                    flag2+=1
                    print(fixed_top_left2, fixed_bottom_right2)
                if flag2!=0 and (btl_2[0]>fixed_top_left2[0]+50 or btl_2[0]<fixed_top_left2[0]-50 or bbr_2[1]>fixed_bottom_right2[1]+50 or bbr_2[1]<fixed_bottom_right2[1]-50):
                    pass #print('bottle has been moved')

        cv2.imshow('frame1', frame1)
        cv2.imshow('frame2', frame2)
        if countbottle1==0 and countbottle2==0:
            if time_flag==0 and time_flag2==0:
                start_time=time.time() # in seconds
                time_flag+=1
            #if time_flag>0:    
            elapsed_time=time.time()

            if elapsed_time-start_time>=10:
                print("ALARM:bottle is not visible for more than 10 seconds in both the frames")
                time_flag=0
                time_flag2=0
            else:
                frame1 = cv2.rectangle(frame1, btl_1, bbr_1, (0,0,255), 5)
                frame1 = cv2.putText(frame1, 'bottle is not visible', btl_1, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
                frame2 = cv2.rectangle(frame2, btl_2, bbr_2, (0,0,255), 5)
                frame2 = cv2.putText(frame2, 'bottle is not visible', btl_2, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('frame1', frame1)
            cv2.imshow('frame2', frame2)

        elif countbottle1==0 and countbottle2!=0:
            frame1 = cv2.rectangle(frame1, btl_1, bbr_1, (0,0,255), 5)
            frame1 = cv2.putText(frame1, 'bottle is not visible', btl_1, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('frame1', frame1)
        elif countbottle2==0 and countbottle1!=0:
            frame2 = cv2.rectangle(frame2, btl_2, bbr_2, (0,0,255), 5)
            frame2 = cv2.putText(frame2, 'bottle is not visible', btl_2, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('frame2', frame2)           
                
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
capture_1.release()
capture_2.release()
cv2.destroyAllWindows()      
