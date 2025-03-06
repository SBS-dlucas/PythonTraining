# file: gevent_app_https.py
from sockettesting import app
from gevent.pywsgi import WSGIServer
import webbrowser

def start_server():
    """
    Starts the app and associated server,
    then opens a web browser to localhost to view the app
    """
    # TODO: try to stop existing instance of server before starting it
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    webbrowser.open_new('http://127.0.0.1:5000/')
    try:
        http_server.serve_forever()
    except Exception as e:
        # This can be reached if the server is already running
        print()