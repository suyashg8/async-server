import asyncio
from responses import Response, JSONResponse, Http404
from request import Request
from functools import partial
from handler import Handler

class EchoServerClientProtocol(asyncio.Protocol):
    
    def __init__(self, handler, loop):
        self.handler = handler
        self.loop = loop
    
    def connection_made(self, transport):
        # peername = transport.get_extra_info('peername')
        # print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        
        # do your thang
        req = Request(message)
        # coro = partial(self.handler.handle, req, self.transport)
        co = self.loop.create_task(self.handler.handle(req, self.transport))
        


class App:
    
    def __init__(self, urls):
        self.urls = urls
        
    def start_server(self):
            
        loop = asyncio.get_event_loop()
        handler = Handler(self.urls)
        
        # Each client connection will create a new protocol instance
        coro = loop.create_server(lambda: EchoServerClientProtocol(handler, loop), '127.0.0.1', 8888)
        server = loop.run_until_complete(coro)

        # Serve requests until Ctrl+C is pressed
        print('Serving on {}'.format(server.sockets[0].getsockname()))
    
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass

        # Close the server
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()
    
    def init_db(self, db_name):
        from db import DB
        db = DB(db_name)
        self.conn = db.get_conn()
