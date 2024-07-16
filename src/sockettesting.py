import socketio
import eventlet


sio = socketio.Server()
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
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', port)), app)


if __name__ == '__main__':
    print('starting server 1 on 65432')
    eventlet.spawn(start_socket_server, 65432)
   # t1 = threading.Thread(target=start_socket_server, args=[65432])
   # t1.start()

    print('starting server 2 on 65433')
    start_socket_server(65433)
   # eventlet.spawn(start_socket_server, [65433])
   # t2 = threading.Thread(target=start_socket_server, args=[65433])
   # t2.start()