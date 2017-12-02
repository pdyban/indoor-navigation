from roomsearchservice import search, HOST_NAME, HOST_PORT
import asyncio
import websockets


async def processor(websocket, _path):
    while True:
        descriptor = await websocket.recv()
        print("< User searches room named {}".format(descriptor))
        rooms = search(descriptor, 'rooms.db')
        reply = ';'.join(rooms)
        await websocket.send(reply)
        print("> {}".format(reply))


def run_server():
    start_server = websockets.serve(processor, HOST_NAME, HOST_PORT)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    run_server()
