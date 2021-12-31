#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from com_server import Connection, RestApiHandler
from com_server.api import Builtins
from flask import Response, jsonify

from camera import VCam

conn = Connection(115200, "/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1", send_interval=0)

handler = RestApiHandler(conn, has_register_recall=False, add_cors=True, catch_all_404s=True)
Builtins(handler)

manual = True

def stream_gen(cam: VCam):
    while True:
        global manual
            
        frame = cam.next_frame(manual)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        time.sleep(0.01)

@handler.flask_obj.route("/stream")
def stream():
    return Response(stream_gen(VCam(conn)), mimetype='multipart/x-mixed-replace; boundary=frame')

@handler.flask_obj.route("/manual_state")
def manual_state():
    return jsonify({"manual": manual});

@handler.flask_obj.route("/manual_toggle")
def toggle_manual():
    global manual
    manual  = not manual

    time.sleep(0.5)

    conn.send("l:0;r:0", ending='\n')
    return jsonify({"manual": manual});

if __name__ == "__main__": 
    handler.run_prod(host="0.0.0.0", port=7123)

