#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time

cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

class VCam():
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        print("stopping video")
        self.video.release()

    def next_frame(self, manual):
        global cascade

        if not manual:
            print("here", time.time())
            
        _, image = self.video.read()

        # dimensions (w, h) should be (640, 480)
        hei, wid, _ = image.shape

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        is_good_left = False
        is_good_right = False
        if (len(faces) > 0):
            x, y, w, h = faces[0]

            # bounding boxes
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # toleration lines
            if (x-10 >= 0):
                cv2.line(image, (x-10, 0), (x-10, hei), (235, 183, 0), 2)

            if (x+10 < wid):
                cv2.line(image, (x+w+10, 0), (x+w+10, hei), (235, 183, 0), 2)

            is_good_left = (wid//2 >= x-10)
            is_good_right = (wid//2 <= x+w+10)


        if (is_good_left != is_good_right):
            middle_color = (0, 0, 255)
        elif (not is_good_left):
            middle_color = (155, 155, 155)
        else:
            middle_color = (0, 255, 0)

        # center line - where the robot is facing
        cv2.line(image, (wid//2, 0), (wid//2, hei), middle_color, 2)

        _, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()
    
