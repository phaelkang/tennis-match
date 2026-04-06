import os
os.chdir("/Users/phaelkang/Desktop/Claude")
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(("", 8080), SimpleHTTPRequestHandler).serve_forever()
