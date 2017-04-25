from inspect import isawaitable
from responses import Http404

class Handler:
  
  def __init__(self, urls):
    self.urls = urls
  
  def get_handler(self, request):
    path = request.headers['path']
    for url in self.urls:
      if url[0] == path:  # use regex here
        return url[1]
  
  
  async def handle(self, request, transport):
    
    handler = self.get_handler(request)
    
    if not handler:
      resp = Http404()
    
    else:
      resp = handler(request)
      
      if isawaitable(resp):
        resp = await resp
    
    transport.write(resp.make_response())
    transport.close()
      
