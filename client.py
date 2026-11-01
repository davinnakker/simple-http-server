import socket
import json

def build_post_test_request():
    body_py_obj = {
        "id": 2345,
        "text": "wow that's crazy",
    }
    body = json.dumps(body_py_obj)
    content_len = len(body.encode())
    request = "POST /api/v1/post HTTP/1.1\r\n" + \
            "Content-Type: application/json\r\n" + \
            f"Content-Length: {content_len}\r\n\r\n" + \
            body
    return request

def build_get_test_request():
    request = "GET /api/v1/post/4 HTTP/1.1\r\n" + \
            "Authorization: Bearer 49fj39\r\n\r\n"
    return request

def run_client(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("localhost", 5000))

        print("Sending message...")
        client.sendall(request.encode())
        print("Message Sent")

        data_in_bytes = client.recv(1000)
        print(f"Server Responded: {data_in_bytes.decode()}")

if __name__ == "__main__":
    post_request = build_post_test_request()
    run_client(post_request)
    get_request = build_get_test_request()
    run_client(get_request)
