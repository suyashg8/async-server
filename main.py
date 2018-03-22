import asyncio
from io import StringIO
from responses import Response, JSONResponse, Http404
from request import Request
from utils import match_url

class EchoServerClientProtocol(asyncio.Protocol):
    
    def __init__(self, urls):
        self.urls = urls
    
    def connection_made(self, transport):
        # peername = transport.get_extra_info('peername')
        # print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        
        # do your thang
        req = Request(message)
        print(req.headers['full_path'])
        view = match_url(self.urls, req.headers['path'])
        # check if valid handler
        if not view:
            resp = Http404()
        else:
            resp = view(req)
        self.transport.write(resp.make_response())
        
        
        self.transport.close()


class App:
    
    def __init__(self, urls):
        self.urls = urls
        
    def start_server(self):
            
        loop = asyncio.get_event_loop()
        # loop.set_debug(True)
        
        # Each client connection will create a new protocol instance
        coro = loop.create_server(lambda: EchoServerClientProtocol(self.urls), '127.0.0.1', 8012)
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
