import email
from io import StringIO
from urllib.parse import urlparse, parse_qs

class Request:
  
  def __init__(self, req):
    request_line, headers_alone = req.split('\r\n', 1)
    message = email.message_from_file(StringIO(headers_alone))
    headers = dict(message.items())
    headers['method'], headers['full_path'], headers['http-version'] = request_line.split()    
    
    GET = parse_qs(urlparse(headers['full_path']).query)
    post_qs = req.split('\r\n')[-1]
    POST = parse_qs(post_qs)
    
    headers['path'] = headers['full_path'].split('?')[0]
    
    self.headers = headers
    self.full_req_string = req
    self.GET = GET
    self.POST = POST

  def __str__(self):
    return str(self.headers) + '<===>' + str(self.GET) + '<===>' + str(self.POST)
    
  
