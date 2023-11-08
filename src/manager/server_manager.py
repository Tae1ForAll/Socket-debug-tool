import socketio

socket_io = socketio.Client(serializer='msgpack')
callback = None

def connect_server(server_url: str):
    print("server_url: ", server_url)
    socket_io.connect(server_url, transports=['websocket', 'polling'], wait_timeout=10)

def emitReqeust(event_name, request_body, callback):
    socket_io.emit(event_name, request_body, callback=callback)

def onCompleteEmit(data):
    print(data)

def join_room():
    socket_io.emit('requestJoinGame', {
        "pfid": "62130b00bc1acf58340948ae",
        "pfuid": "tae_888",
        "pfutk": "xxxxxxx",
        "gid": "64f83c43e4d49990ad35ee64",
        "wt": "seamless"
    }, callback=on_join_room)

def on_join_room(data):
    print(type(data))

@socket_io.event
def connect():
    print("I'm connected!")
    # join_room()

@socket_io.event
def connect_error(data):
    print(data)
    print("The connection failed!")