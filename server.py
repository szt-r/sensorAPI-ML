import asyncio
import websockets
import settings


async def listening(websocket, path):
    while True:
        msg = await websocket.recv()
        print(f"Message from client: {msg}")
        rcv = f"Message rcv!"
        await websocket.send(rcv)

start_server = websockets.serve(listening, settings.IP_ADDRESS, settings.PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
