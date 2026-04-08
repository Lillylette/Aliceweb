from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
        <!DOCTYPE html>
        <html>
        <head><title>Aliceweb</title></head>
        <body>
        <h1>Aliceweb РАБОТАЕТ!</h1>
        <p>Сервер успешно запущен.</p>
        </body>
        </html>
        ''')

port = int(os.environ.get('PORT', 8080))
print(f'Запуск сервера на порту {port}...')
server = HTTPServer(('0.0.0.0', port), Handler)
print(f'Сервер запущен! Откройте http://localhost:{port}')
server.serve_forever()
