# Local preview: run "python3 serve.py" in this folder, then open http://localhost:8000
# Applies the same rewrite as vercel.json (/x.php -> /x.html).
import http.server, sys, os
class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, p):
        q = p.split('?')[0].split('#')[0]
        if q.endswith('.php'): q = q[:-4] + '.html'
        return super().translate_path(q)
    def log_message(self, *a): pass
os.chdir(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
print(f'Preview running at http://localhost:{port}  (Ctrl+C to stop)')
http.server.ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
