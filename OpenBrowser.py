import http.server
import socketserver
import webbrowser

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# ブラウザを開く
webbrowser.open_new('http://localhost:' + PORT + '/index.html')

# Pythonでhttpサーバーを立てる
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    #print("serving at port", PORT)
    httpd.serve_forever()
