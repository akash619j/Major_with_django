#breaking video into individual frames. COmpression not done yet. will be done in diff_image_2.py

import cv2
import os
def frame_images():
    #os.chdir("/home/akash/PycharmProjects/Djangoproject/Major_Project/Major/main_app")
    cap = cv2.VideoCapture("/home/akash/PycharmProjects/Djangoproject/Major_Project/Major/main_app/downloaded_vid.mp4")
    cap.open("/home/akash/PycharmProjects/Djangoproject/Major_Project/Major/main_app/downloaded_vid.mp4")
    print (cap.isOpened())
    i=0
    while(cap.isOpened()):
        global i
        ret,frame = cap.read()
        frame = cv2.resize(frame, (frame.shape[1]/3, frame.shape[0]/3))
        cv2.imwrite(str(i)+".jpg", frame)     # save frame as JPEG file
        i=i+1
frame_images()