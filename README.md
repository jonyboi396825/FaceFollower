# Face Following Car Project

<img src="https://hackster.imgix.net/uploads/attachments/1391910/_05BRjp9X7Q.blob?auto=compress%2Cformat&w=900&h=675&fit=min" alt="Picture of Face Following Car" width="60%">

Using an Amazon robot chassis kit, I created a face following car by mounting a camera and a Raspberry Pi to process the camera feed. Using OpenCV's face detection library and motor controllers, I programmed the car to continuously turn towards a face.

## Components
- Raspberry Pi 4 Model B
- Raspberry Pi Camera Module
- Arduino Nano
- SparkFun L298N Dual H-Bridge Motor Drivers
- Breadboard
- Jumper Wires
- [Robot Chassis](https://www.amazon.com/perseids-Chassis-Encoder-Wheels-Battery/dp/B07DNXBFQN/ref=sr_1_5?keywords=robot+chassis&qid=1636856040&sr=8-5)

## How it works

I made this robot with a Raspberry Pi 4 and an Arduino. The camera is attached to the Raspberry Pi, and the Raspberry Pi uses OpenCV to detect the faces in the camera. The Arduino acts as the motor driver by receiving commands from the Pi and sending a PWM signal to the L298N controllers. Based on where the faces are, the Raspberry Pi uses the USB port to tell the Arduino how much to move the motors.

To visualize the face detections and the camera feed, I created a website that is hosted on a local server on the Raspberry Pi. I used Flask to implement the backend, which takes in the camera feed and sends it to the frontend (implemented using Vue.js). The website website includes the video stream that has the bounding boxes of the faces calculated from the backend, and it also adds the ability to control the robot manually using the keyboard (WASD keys) by sending requests to the backend.

For the hardware, I used a robot chassis kit that I found on Amazon, which comes with a chassis, 4 wheels, and 4 motors. I used two L298N motor controllers to control all motors, one for the left side, and the other for the right. The Raspberry Pi and motor controllers are powered by AA batteries.

## Videos

[![IMAGE ALT TEXT](http://img.youtube.com/vi/hAqQJSInm0I/0.jpg)](http://www.youtube.com/watch?v=hAqQJSInm0I)
[![IMAGE ALT TEXT](http://img.youtube.com/vi/Vf0bkWuoIJ4/0.jpg)](http://www.youtube.com/watch?v=Vf0bkWuoIJ4)
[![IMAGE ALT TEXT](http://img.youtube.com/vi/-aXtwGO-xwU/0.jpg)](http://www.youtube.com/watch?v=-aXtwGO-xwU)

## Schematics

![facefollowerschematic_JsJUhf1D03](https://github.com/jonyboi396825/FaceFollower/assets/81734282/415c1ff1-e3e3-45d2-b182-0017c077fdc1)
