import asyncio
import pathlib
import ssl
import websockets
import settings


async def listening(websocket, path):
    while True:
        msg = await websocket.recv()
        print(f'Message from client: {msg}')
        rcv = f"Message rcv!"
        await websocket.send(rcv)


print(f"Server on: {settings.IP_ADDRESS}:{settings.PORT}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name('localhost.pem')
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(
    listening, settings.IP_ADDRESS, settings.PORT, ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
