
#Nemo , Jan 26 2018


import sendsms
import datetime
import cv2
import numpy as np
import easygui

# this is the main part of the app which detect the motion and send msg to a given phone number
# The parameter is gs_window,gs_sig,diff_thresh,min_area,mod, check the main.py for instruction


def motion_detection(gs_window,gs_sig,diff_thresh,min_area,mod):

    flag = 1

    camera = cv2.VideoCapture(0)

    if (camera.isOpened()) == False:
        easygui.msgbox("Please turn on your camera, and if you dont know how, please get out of my sight xD")

    size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('size:' + repr(size))

    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 4))
    kernel = np.ones((5, 5), np.uint8)
    background = None

    while True:

        text = "Undetected"
        grabbed, frame_lwpCV = camera.read()

        gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY)
        gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (gs_window, gs_window), gs_sig)
        # gray_lwpCV = cv2.blur(gray_lwpCV, (10, 50))

        if background is None:
            background = gray_lwpCV
            continue

        diff = cv2.absdiff(background, gray_lwpCV)
        diff = cv2.threshold(diff, diff_thresh, 255, cv2.THRESH_BINARY)[1]
        diff = cv2.dilate(diff, es, iterations=2)

        image, contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < min_area:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame_lwpCV, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Detected"

        if text == 'Undetected':
            cv2.putText(frame_lwpCV, "Motion: {}".format(text), (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame_lwpCV, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, frame_lwpCV.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)

        if text == 'Detected':
            cv2.putText(frame_lwpCV, "Motion: {}".format(text), (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame_lwpCV, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, frame_lwpCV.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            if flag == 1 and mod == 1:
                sendsms.sendsms()

        cv2.imshow('contours', frame_lwpCV)
        cv2.imshow('dis', diff)

        key = cv2.waitKey(1) & 0xFF
        # 按'q'健退出循环
        if key == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()