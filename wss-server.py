import asyncio
import pathlib
import ssl
import websockets
import settings
import sys


async def listening(websocket, path):
    gesture_type = sys.argv[1]
    sample_number = int(sys.argv[2])
    # prev_sample_number = sample_number
    while True:
        file_path = f'./data/data_{gesture_type}_{sample_number}.txt'
        client_msg = await websocket.recv()
        print(f'Message from client: {client_msg}')
        await websocket.send(f'Received!')
        if client_msg != 'end':
          with open(file_path, 'a') as output_file:
            output_file.write(client_msg + '\n')
        else:
          sample_number += 1


print(f'Server on: {settings.IP_ADDRESS}:{settings.PORT}')

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name('localhost.pem')
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(
    listening, settings.IP_ADDRESS, settings.PORT, ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
