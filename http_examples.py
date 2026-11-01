"""
GET /api/v1/post/3 HTTP/1.1
Host: api.example.com
Accept: application/json
Authorization: Bearer 35jij35ij
"""

request_header = {
    "type": "GET",
    "body": False,
    "resource": "api/v1/post/3",
    "version": "HTTP/1.1",
    "headers": {
        "Host": "api.example.com",
        "Accept": "application/json",
        "Authorization": "Bearer 35jij35ij",
    }
}

request_body = {
    
}