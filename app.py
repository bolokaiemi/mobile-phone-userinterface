import http.server
import socketserver
import os


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

class NoCacheHTTPRequestHandler(Handler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    # Ensure working directory is the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Starting development server at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    try:
        with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
