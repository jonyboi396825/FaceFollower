#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from com_server import Connection, RestApiHandler, Builtins

def main():
    # order of priority
    # first try USB0, then USB1, then ACM0, then ACM1

    conn = Connection(115200, "/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1", send_interval=0.1)

    handler = RestApiHandler(conn, has_register_recall=False, add_cors=True)
    Builtins(handler)
     
    handler.run_prod(host="0.0.0.0", port=7123)

if __name__ == "__main__":
    main()

