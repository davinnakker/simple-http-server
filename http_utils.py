"""
HTTP UTILITIES

This module just consists of function help create and parse HTTP requests
"""

import json


def parse_request_header(raw_header: str):
    """
    Parses Headers and decides if there is a body
    """
    header_obj = {}
    lines = raw_header.split("\r\n")
    first_line = lines.pop(0)
    type, resource, version = first_line.split()
    headers = {}
    for header in lines:
        key, value = header.split(": ")
        headers[key] = value
    if "Content-Length" in headers.keys():
        header_obj["body"] = True
    else:
        header_obj["body"] = False
    header_obj["type"] = type
    header_obj["resource"] = resource
    header_obj["version"] = version
    header_obj["headers"] = headers
    return header_obj


def parse_request_body(body: str):
    """
    Only parses json for now.
    """
    return json.loads(body)



def run_tests():
    example = "GET /api/v1/post/3 HTTP/1.1\r\n" + \
              "Host: api.example.com\r\n" + \
              "Accept: application/json\r\n" + \
              "Authorization: Bearer 35jij35ij"
    print(parse_request_header(example)) 

if __name__ == "__main__":
    run_tests()
    


    