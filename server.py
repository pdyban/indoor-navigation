
# coding: utf-8

# In[1]:


import websockets
import asyncio


# The following is the backend processor service. It receives a message from the frontend (nodes A and B) and returns the result, i.e. the shortest path between the requested nodes.

# In[ ]:


import IndoorGraph as ig


# In[ ]:


async def processor(websocket, _path):
    nodes = await websocket.recv()
    print("< {}".format(nodes))
    node_source, node_target = nodes.split(':')
    graph = ig.create_graph('test_graph.json')
    print(graph)
    path = ig.compute_shortest_path(graph, (node_source, node_target))
    print(path, graph)
    reply = "The shortest path is {}!".format(path)
        
    await websocket.send(reply)
    print("> {}".format(reply))    


def run_server(host_name=ig.HOST_NAME, port=ig.PORT):

    start_server = websockets.serve(processor, host_name, port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    run_server()
