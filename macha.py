import asyncio

from collectiosn import namedtuple
from io import BytesIO
from socket import error as socket_error




class CommandError(Exception):
    pass

class Disconnect(Exception):
    pass

Error = namedtuple('Error' , ('message',))


class ProtocolHandler:
    def handle_request(self,socket_file):
        # parse a request from the client into its component parts
        pass

    def write_response(self,socket_file,data):
        # serialize the response data and send it to the client
        pass


class Server:
    def __init__(Self,host='127.0.0.1',port=31337,max_clients=64):
        self._pool = Pool(max_clients)
        self._server = StreamServer()



async def main():
    print('hello')
    await asyncio.sleep(1)
    print("world")


if __name__ == '__main__':
   asyncio.run( main())
