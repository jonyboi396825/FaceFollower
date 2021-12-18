#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

class VCam():
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        print("stopping video")
        self.video.release()

    def next_frame(self):
        global cascade
            
        _, image = self.video.read()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        _, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()
    
