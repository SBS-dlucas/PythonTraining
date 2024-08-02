import socketio
import eventlet
from engineio.async_drivers import threading
import eventlet.wsgi
import socketserver
import http.server

sio = socketio.Server(async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def send_command(sid, data):
    if (data == 'gethd'):
        sio.emit('command_response', 'imagine a gethd response here', to=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)


def start_socket_server(port):
    try:
        eventlet.wsgi.server(eventlet.listen(('127.0.0.1', port)), app)
    except:
        # something went wrong, maybe the socket is already open
        print('something went wrong, maybe the socket is already open')


if __name__ == '__main__':
    print('starting server 1 on 65432')
    eventlet.spawn(start_socket_server, 65432)

    print('starting server 2 on 65433')
    eventlet.spawn(start_socket_server(65433))

    # If we need to spawn more servers, continue with spawning them on threads
    # eventlet.spawn(start_socket_server, [65433])
