from responses import HTMLResponse

class Template:
  
  def __init__(self, file_name):
    self.file_name = file_name
  
  
  def render_to_string(self, content, context):
    for key in context.keys():
      content = content.replace( "{% " + key + " %}", str(context[key]) )
    
    return content
  
  def render(self, context):
    with open(self.file_name, 'r') as fp:
      lines = fp.readlines()
    
    lines = "".join(lines)
    return HTMLResponse(self.render_to_string(lines, context))
