import asyncio
import threading  # the server must run in a separate thread in order not to block execution

from routingservice import server, client


class ServerThread(threading.Thread):
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        server.run_server()


if __name__ == '__main__':
    print('Starting server')
    st = ServerThread()
    st.start()
    print('Server launched')
    print('Starting client')
    client.run_client()
    print('Client executed')
    # st.stop()
    st.join()
    print('Server closed')
