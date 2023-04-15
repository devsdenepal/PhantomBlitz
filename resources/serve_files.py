def serve_http():
    import http.server
    import socketserver
    HTTP_PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", HTTP_PORT), Handler) as httpd:
        print("serving at port", HTTP_PORT)
        httpd.serve_forever()
