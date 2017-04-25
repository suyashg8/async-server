from main import App
from responses import JSONResponse, Response

def jsu(request):
  return JSONResponse({'first':'resp', 'hello':'world', 'yay':'yuppie'})

def nojsu(request):
  
  if request.POST:
    return Response('text/html', "<p style='color:#d3d3d3'>{}</p>".format(str(request.POST)))
  else:
    return Response('text/html', "<p style='color:#d3d3d3'>Getter</p>")

urls = [
        ('/hello', jsu),
        ('/post', nojsu)
        ]

app = App(urls)

app.start_server()
