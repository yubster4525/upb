import http.server
import threading

_progress = {
    "stage": None,
    "iteration": 0,
    "mean_reward": 0.0,
}

class ProgressHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        html = "<html><head><title>Training Progress</title><meta http-equiv='refresh' content='1'></head><body>"
        html += "<h1>Training Progress</h1>"
        for key, val in _progress.items():
            if val is not None:
                html += f"<p><strong>{key}</strong>: {val}</p>"
        html += "</body></html>"
        body = html.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        # Quiet handler
        return

def start_server(port=8000):
    server = http.server.HTTPServer(("", port), ProgressHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server

def stop_server(server):
    if server is not None:
        server.shutdown()

def update_progress(**kwargs):
    _progress.update(kwargs)
