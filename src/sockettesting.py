import sys, io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()

from flask import Flask, render_template
from flask_socketio import SocketIO
from flaskwebgui import FlaskUI
import plotly.graph_objs as go
import plotly.io as pio
import webbrowser
from threading import Timer
from engineio.async_drivers import threading

import os

# cool hack because pyinstaller deletes stdout and stderr
'''if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode="threading")

@app.route('/')
def index():
    # Create a simple plotly graph
    fig = go.Figure(data=[go.Bar(x=['A', 'B', 'C'], y=[1, 3, 2])])
    graph_html = pio.to_html(fig, full_html=False)
    return render_template('index.html', graph_html=graph_html)

@socketio.on('connect')
def connect():
    print('Client connected')
    # Send initial chart data
    fig = go.Figure(data=[go.Bar(x=['A', 'B', 'C'], y=[1, 3, 2])])
    graph_json = fig.to_json()
    socketio.emit('update_chart', graph_json)

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

@socketio.on('my_message')
def handle_my_message(data):
    print('message ', data)

@socketio.on('send_command')
def handle_send_command(data):
    if data == 'gethd':
        socketio.emit('command_response', 'imagine a gethd response here')

@socketio.on('update_chart_server')
def handle_send_command(data):
    socketio.emit('update_chart', data)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:65432/')

def start_flask():

    # app = server_kwargs.pop("app", None)
    # local_socketio = server_kwargs.pop("socketio", None)
    # server_kwargs.pop("debug", None)
    
    socketio.run(app, port=65432, allow_unsafe_werkzeug=True)  # Start the server


if __name__ == '__main__':
    # Timer(1, open_browser).start()  # Open the browser after 1 second
    
    FlaskUI(
        app=app,
        start_server='flask-socketio',
        socketio=socketio,
        port=65432,
        width=800,
        height=600,
        close_server_on_exit=False,
        idle_interval=50
    ).run()
    
   # socketio.run(app, port=65432, debug=True, allow_unsafe_werkzeug=True)  # Start the server
