import http.server
import socketserver
import json


class my_new_class(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            new_dataset = json.dumps(data)
            my_content = new_dataset
            content_type = "application/json"
            self.response(my_content, content_type)
        elif self.path == "/info":
            data = {"version": "1.0", "description": "A simple "
                    "API built with http.server"}
            new_dataset = json.dumps(data)
            my_content = new_dataset
            content_type = "application/json"
            self.response(my_content, content_type)
        elif self.path == "/status":
            my_content = "OK"
            content_type = "text/plain"
            self.response(my_content, content_type)
        elif self.path == "/":
            my_content = "Hello, this is a simple API!"
            content_type = "text/plain"
            self.response(my_content, content_type)

        else:
            my_content = "Endpoint not found"
            content_type = "text/plain"
            self.response(my_content, content_type, 404)

    def response(self, my_content, content_type, status_code=200):
        my_content_bytes = my_content.encode('utf-8')
        self.send_response(status_code)
        if content_type == "application/json":
            self.send_header("Content-type", content_type)
        else:
            self.send_header("Content-type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(my_content_bytes)))
        self.end_headers()
        self.wfile.write(my_content_bytes)


PORT = 8000
with socketserver.TCPServer(("", PORT), my_new_class) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
