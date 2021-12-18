#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from com_server import Connection, RestApiHandler, Builtins
from flask import Flask, render_template, Response

from camera import VCam

conn = Connection(115200, "/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1", send_interval=0.1)

handler = RestApiHandler(conn, has_register_recall=False, add_cors=True, catch_all_404s=True)
Builtins(handler)

def stream_gen(cam: VCam):
    while True:
        frame = cam.next_frame()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        time.sleep(0.01)

@handler.flask_obj.route("/stream")
def stream():
    return Response(stream_gen(VCam()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__": 
    handler.run_prod(host="0.0.0.0", port=7123)

