from com_server import Connection

class Mover:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def stop(self) -> None:
        self.conn.send("l:0;r:0", ending='\n')

    def moveR(self) -> None:
        self.conn.send("l:255;r:0", ending='\n')

    def moveL(self) -> None:
        self.conn.send("l:0;r:255", ending='\n')

