#!/usr/bin/env python3
"""Local preview with extensionless URLs and _redirects, similar to Cloudflare Pages."""

import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("PORT", "8080"))


def load_redirects():
    rules = []
    path = os.path.join(ROOT, "_redirects")
    if not os.path.isfile(path):
        return rules
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 3:
            rules.append((parts[0], parts[1], parts[2]))
    return rules


REDIRECTS = load_redirects()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def _redirect(self):
        path = self.path.split("?", 1)[0]
        for src, dest, code in REDIRECTS:
            if path == src:
                self.send_response(int(code))
                self.send_header("Location", dest)
                self.send_header("Content-Length", "0")
                self.end_headers()
                return True
        return False

    def do_HEAD(self):
        if self._redirect():
            return
        super().do_HEAD()

    def do_GET(self):
        if self._redirect():
            return
        super().do_GET()

    def translate_path(self, path):
        clean = path.split("?", 1)[0].split("#", 1)[0]
        rel = clean.lstrip("/")
        if rel == "":
            return os.path.join(ROOT, "index.html")
        direct = os.path.join(ROOT, rel)
        if os.path.isfile(direct):
            return direct
        html_path = direct + ".html" if not rel.endswith(".html") else direct
        if os.path.isfile(html_path):
            return html_path
        return direct


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Preview http://127.0.0.1:{PORT}/")
    server.serve_forever()
