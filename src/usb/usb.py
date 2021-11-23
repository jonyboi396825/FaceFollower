#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from com_server import Connection, RestApiHandler, Builtins

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

    handler = RestApiHandler(conn)
    Builtins(handler)
    
    handler.run_prod(host="127.0.0.1", port=7123)

if __name__ == "__main__":
    main()

