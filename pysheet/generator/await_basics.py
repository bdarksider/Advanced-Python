# yield from == await expression

import asyncio
import socket

# set socket and event loop
loop = asyncio.get_event_loop()
host = 'localhost'
port = 5566
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(False)
sock.bind((host, port))
sock.listen(10)

@asyncio.coroutine
def echo_server():
    while True:
        conn, addr = yield from loop.sock_accept(sock)
        loop.create_task(handler(conn))

@asyncio.coroutine
def handler(conn):
    while True:
        msg = yield from loop.sock_recv(conn, 1024)
        if not msg:
            break
        yield from loop.sock_sendall(conn, msg)
    conn.close()

# equal to
async def echo_server():
    while True:
        conn, addr = await loop.sock_accept(sock)
        loop.create_task(handler(conn))

async def handler(conn):
    while True:
        msg = await loop.sock_recv(conn, 1024)
        if not msg:
            break
        await loop.sock_sendall(conn, msg)
    conn.close()

loop.create_task(echo_server())
loop.run_forever()
