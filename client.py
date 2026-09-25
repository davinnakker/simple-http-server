import socket
from http_utils import RequestMethod, create_request

def run_client(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("localhost", 5000))

        print("Sending message...")
        client.sendall(request.encode())
        print("Message Sent")

        data_in_bytes = client.recv(1000)
        print(f"Server Responded: {data_in_bytes.decode()}")

if __name__ == "__main__":
    http_request_string = create_request(RequestMethod.POST, "/users", "application/json", { "user_id": 88893 })
    run_client(http_request_string)