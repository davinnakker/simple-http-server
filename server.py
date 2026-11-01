"""
HTTP SERVER

See Architecture Diagram -> server.md

-- Server --
This function will create the main socket that bind to an address. Using a loop it will accept
incoming connections and spawn a new socket connection and pass it two a new child thread.

-- Connection --
This is a threaded class that will use the new socket connection passed by the server and process
incoming http requests. 
It should perform the following:
    - receive bytes until end point is identified
    - parse http request
    - route request to resource
    - construct a response
    - send the http response

"""

import socket
import threading

from http_utils import parse_request_header, parse_request_body

IP_ADDRESS = "0.0.0.0"
PORT = 5000

class ConnectionWorker(threading.Thread):
    def __init__(self, connection: socket.socket, address):
        super().__init__()
        self.connection = connection
        self.address = address
        self.body = None
        self.header = None
        self.header_obj = None
        self.body_obj = None

    def run(self):
        """
        Starts by receiving bytes until the header is found. 
        Uses the parse_request_header helper to turn the raw 
        header into an organized header object. 

        If header object indicates there is a body attached then it 
        will receive the body up to the indicated content length.
        Uses the parse_request_body helper to turn the raw body
        into and organized object.
        """
        print(f"Address {self.address} Thread to Receive...")
        header, extra = self._receive_bytes_till()
        self.header = header
        header_obj = parse_request_header(header)
        self.header_obj = header_obj
        print(self.header_obj)
        if header_obj["body"]:
            content_length = header_obj.get("headers", {}).get("Content-Length", 0)
            body = self._receive_bytes_amount(byte_limit=int(content_length), starting_bytes=extra.encode())
            self.body = body
            body_obj = parse_request_body(body)
            self.body_obj = body_obj
            print(self.body_obj)

    def _receive_bytes_till(self, end_pattern = "\r\n\r\n"):
        """
        Using the Connection Socket it will receive bytes from the connection 
        until it contains the 'end pattern'. Once it has received the end pattern
        it will return the string form of all bytes before the 'end pattern' as well
        as a string of the extra bytes if any after the end_pattern.
        """
        with self.connection:
            header_bytes = b""
            while b"\r\n\r\n" not in header_bytes:
                chunk = self.connection.recv(1000)
                if not chunk: # empty chunk means client disconnected
                    break
                header_bytes += chunk

            header, _, extra = header_bytes.decode().partition(end_pattern)
            return header, extra

    def _receive_bytes_amount(self, byte_limit: int, starting_bytes: b""):
        """
        Using the Connection Socket it will receive bytes from the connection 
        until it has reaches the 'byte limit' and will then return that number 
        of bytes received as a string.
        """
        with self.connection:
            body_bytes = starting_bytes
            while len(body_bytes) < byte_limit:
                chunk = self.connection.recv(100)
                if not chunk:
                    break
                body_bytes += chunk

            body = body_bytes[:byte_limit].decode()
            return body


def run_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        
        server.bind((IP_ADDRESS, PORT))
        server.listen()
        print(f"Server Listening on {IP_ADDRESS}:{PORT}\n")

        while True:
            connection, address = server.accept()
            print(f"\nAddress: {address} has connected")
            thread = ConnectionWorker(connection, address)
            thread.start()

if __name__ == "__main__":
    run_server()
