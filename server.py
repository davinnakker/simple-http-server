import socket
import threading

from http_utils import RequestMethod, parse_request, parse_request_header, parse_request_body

IP_ADDRESS = "0.0.0.0"
PORT = 5000

class RequestWorker(threading.Thread):
    def __init__(self, connection: socket.socket):
        super().__init__()
        self.connection = connection
        self.body = None
        self.header = None

    def run(self):
        with self.connection:
            header_bytes = b""
            while b"\r\n\r\n" not in header_bytes:
                chunk = self.connection.recv(8192)

                if not chunk:
                    break

                header_bytes += chunk
            header, _, extra = header_bytes.decode().partition("\r\n\r\n")
            header_obj = parse_request_header(header)
            self.header = header_obj

            if header_obj["method"] == RequestMethod.POST and "Content-Length" in header_obj:
                content_length = int(header_obj['Content-Length'])
                body_bytes = extra.encode()
                while len(body_bytes) < content_length:
                    chunk = self.connection.recv(5000)

                    if not chunk:
                        break

                    body_bytes += chunk
                body_bytes = body_bytes[:content_length] # content length not included bc index starts at zero
                body = body_bytes.decode()
                self.body = parse_request_body(body)


def handler(request_object: dict, connection: socket):
    match request_object["method"]:
        case RequestMethod.GET.value:
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {request_object['body']}\r\n"
                "\r\n"
                "<h1>Hello Lidia! TE AMO <3</h1>"
            )
            connection.sendall(response.encode())
        case RequestMethod.POST.value:
            connection.sendall(b"Thanks for submitting a POST request")
        case _:
            connection.sendall(b"That wasn't a valid request")
    

def run_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        
        server.bind((IP_ADDRESS, PORT))
        server.listen()
        print(f"Server Listening on {IP_ADDRESS}:{PORT}\n")

        while True:
            connection, address = server.accept()
            print(f"\nAddress: {address} has connected")
            thread = RequestWorker(connection)
            thread.start()

            with connection:
                # new tcp connection made / use connection to communicate
                data_in_bytes = b""
                while b"\r\n\r\n" not in data_in_bytes:
                    chunk = connection.recv(1000)
                    data_in_bytes += chunk

                message_string = data_in_bytes.decode()
                response_object = parse_request(message_string)
                print(f"Client sent: \n{message_string}")

                #handler
                handler(response_object, connection)

if __name__ == "__main__":
    run_server()
