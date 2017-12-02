# coding: utf-8

import asyncio
import websockets
import IndoorGraph as ig


async def client():
    async with websockets.connect('ws://{0}:{1}'.format(ig.HOST_NAME, ig.PORT)) as websocket:
        node_a = input("Enter node A:")
        node_b = input("Enter node B:")
        await websocket.send('{}:{}'.format(node_a, node_b))
        print("> ({},{})".format(node_a, node_b))

        path = await websocket.recv()
        print("< {}".format(path))


def run_client():
    asyncio.get_event_loop().run_until_complete(client())


if __name__ == '__main__':
    run_client()
