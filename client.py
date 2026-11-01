import socket
import json
from render_html import render_in_browser

def run_client(request: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("localhost", 5000))

        print("Sending message...")
        client.sendall(request.encode())
        print("Message Sent")

        data_in_bytes = client.recv(8000)
        print(f"Server Responded: {data_in_bytes.decode()}")
        return data_in_bytes.decode()
