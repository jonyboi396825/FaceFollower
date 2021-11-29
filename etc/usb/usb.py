#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# also handles straming

from com_server import Connection, RestApiHandler, Builtins
from flask_cors import CORS
from flask import request, make_response, Response
from picamera import PiCamera

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



def main():
    # order of priority
    # first try USB0, then USB1, then ACM0, then ACM1
    ports = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1"]

    conn = Connection(115200, ports[0])

    for port in ports:
        try:
            conn = Connection(115200, port, send_interval = 0.1)
            conn.connect()
            break
        except:
            pass

    if (not conn.connected):
        raise EnvironmentError("Arduino not found")

    handler = RestApiHandler(conn, has_register_recall=False)
    Builtins(handler)
    CORS(handler.flask_obj)
    
    @handler.flask_obj.route("/video_feed")
    def video_feed():
        return Response(gen(PiCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')
 
    handler.run_prod(host="0.0.0.0", port=7123)

if __name__ == "__main__":
    main()

