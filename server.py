from loguru import logger
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import webbrowser
import urllib
import os
import json


def strava_oauth2(client_id=None, client_secret=None):
    """Run strava authorization flow. This function will open a default system
    browser alongside starting a local webserver. The authorization procedure will be completed in the browser.

    The access token will be returned in the browser in the format ready to copy to the .env file.
    
    Parameters:
    -----------
    client_id: int, if not provided will be retrieved from the STRAVA_CLIENT_ID env viriable
    client_secret: str, if not provided will be retrieved from the STRAVA_CLIENT_SECRET env viriable
    """
    if client_id is None:
        client_id = os.getenv('STRAVA_CLIENT_ID', None)
        if client_id is None:
            raise ValueError('client_id is None')
    if client_secret is None:
        client_secret = os.getenv('STRAVA_CLIENT_SECRET', None)
        if client_secret is None:
            raise ValueError('client_secret is None')
    
    _request_strava_authorize(client_id)

    PORT = 8000

    with Server(("localhost", PORT), HTTPRequestHandler) as httpd:
        logger.info(f"serving at port {PORT}")
        httpd.serve_forever(client_id, client_secret)


def _request_strava_authorize(client_id):
    params_oauth = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": "http://localhost:8000/authorization_successful",
        "scope": "read,profile:read_all,activity:read",
        "state": 'https://github.com/sladkovm/strava-http',
        "approval_prompt": "force"
    }
    values_url = urllib.parse.urlencode(params_oauth)
    base_url = 'https://www.strava.com/oauth/authorize'
    rv = base_url + '?' + values_url
    webbrowser.get().open(rv)
    return None


class Server(HTTPServer):
    def serve_forever(self, client_id, client_secret):
        self.RequestHandlerClass.client_id = client_id
        self.RequestHandlerClass.client_secret = client_secret
        HTTPServer.serve_forever(self)


class HTTPRequestHandler(BaseHTTPRequestHandler):
    client_id = None
    client_secret = None

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        logger.debug(f"path: {url.path}")
        qs = urllib.parse.parse_qs(url.query)
        logger.debug(f"query strings: {qs}")

        if url.path == "/authorization_successful":
            code = qs.get('code')[0]
            logger.debug(f"code: {code}")
            params = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": code,
                "grant_type": "authorization_code"
            }
            r = requests.post("https://www.strava.com/oauth/token", params)
            d = json.loads(r.text)
            logger.debug(f"Authorized athlete: {d.get('access_token', 'Oeps something went wrong!')}")
            rv = f"STRAVA_ACCESS_TOKEN={d.get('access_token', 'Oeps something went wrong!')}".encode()
        else:
            rv = url.path.encode()

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(rv)


if __name__ == "__main__":

    strava_oauth2()