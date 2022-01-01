from com_server import Connection

SP = "100"

class Mover:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def stop(self) -> None:
        self.conn.send("l:0;r:0", ending='\n')

    def moveR(self) -> None:
        self.conn.send(f"l:{SP};r:-{SP}", ending='\n')

    def moveL(self) -> None:
        self.conn.send(f"l:-{SP};r:{SP}", ending='\n')

