from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('192.168.1.79', 4443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(
    httpd.socket, certfile='./localhost.pem', server_side=True)
print('Serving at port', 4443)
httpd.serve_forever()
