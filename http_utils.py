"""
HTTP UTILITIES

This module just consists of function help create and parse HTTP requests
"""

from enum import Enum
import json

class RequestMethod(Enum):
    POST = "POST"
    GET = "GET"


def create_request(method: RequestMethod, resource: str, data_type: str = None, payload: dict | str = ""):
    start_line = f"{method.value} {resource} HTTP/1.1"
    if method == RequestMethod.GET:
        return start_line + "\r\n\r\n"
    
    elif method == RequestMethod.POST:
        header = start_line + "\r\n" + f"Content-Type: {data_type}"
        body = json.dumps(payload)
        return header + "\r\n\r\n" + body


def parse_request_header(header):
    pass


def parse_request_body(body):
    pass


def run_tests():
    pass


if __name__ == "__main__":
    run_tests()
    


    