def handler(header_obj, body_obj):
    if header_obj["type"] == "GET" and header_obj["resource"] == "/api/v1/post":
        return {
            "title": "at the beach",
            "comment": "nice"
        }
    elif header_obj["type"] == "POST" and header_obj["resource"] == "/api/v1/post/1":
        return {
            "message": "post succesfully saved"
        }
    elif header_obj["type"] == "GET" and header_obj["resource"] == "/pages/index.html":
        html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>My Page</title>
            </head>
            <body>
                <h1>Hi, welcome to my page!</h1>
            </body>
            </html>
            """
        return {
            "content": html
        }
    else:
        return {
            "message": "Error: Couldn't find resource"
        }
