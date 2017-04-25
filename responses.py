import json

class Response:
  
  def __init__(self, content_type = 'octet-stream', content = None):
    
    self.headers = dict()
    self.headers['Content-Type'] = content_type
    self.headers['Connection'] = 'close'
    self.headers['Content-Length'] = len(content)
    
    self.status = dict()
    self.status['response-code'] = '200'
    self.status['text'] = 'OK'
    self.status['response_proto'] = 'HTTP/1.1'
    
    self.content = content
  
  
  def make_response(self):
    response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in self.headers.items())
    status_line = '%s %s %s' % (self.status['response_proto'], self.status['response-code'], self.status['text'])
    
    response = status_line + '\n' + response_headers_raw + "\n" + self.content
    
    return bytes(response, 'utf-8')
  

class JSONResponse(Response):
  
  def __init__(self, content):
    
    if type(content) == 'dict':
      import json
      content = json.dumps(content)
    elif type(content) != 'str':
      content = str(content)

    super(JSONResponse, self).__init__('application/json', content)

class Http404(Response):
  def __init__(self, content=''):
    super(Http404, self).__init__('application/json', content)
    self.status['response-code'] = 404
    
