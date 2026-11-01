import json
import webbrowser
import tempfile

from client import run_client

def _render_in_browser(html):

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".html",
        delete=False
    ) as file:

        file.write(html)
        filepath = file.name

    webbrowser.open("file://" + filepath)

def test_page_request():
    request = "GET /pages/index.html HTTP/1.1\r\n" + \
            "Authorization: Bearer 49fj39\r\n\r\n"
    raw_response = run_client(request)
    response_obj = json.loads(raw_response)
    print(response_obj)
    html = response_obj["content"]
    _render_in_browser(html)

def test_post_request():
    body_py_obj = {
        "id": 2345,
        "text": "wow that's crazy",
    }
    body = json.dumps(body_py_obj)
    content_len = len(body.encode())
    request = "POST /api/v1/post/1 HTTP/1.1\r\n" + \
            "Content-Type: application/json\r\n" + \
            f"Content-Length: {content_len}\r\n\r\n" + \
            body
    raw_response = run_client(request)
    response_obj = json.loads(raw_response)
    print(response_obj)

def test_get_request():
    request = "GET /api/v1/post HTTP/1.1\r\n" + \
            "Authorization: Bearer 49fj39\r\n\r\n"
    raw_response = run_client(request)
    print(raw_response)
    response_obj = json.loads(raw_response)
    print(response_obj)

if __name__ == "__main__":
    test_get_request()
    test_post_request()
    test_page_request()