import asyncio
from main import App
from responses import JSONResponse, Response
from responses import Http404
from templates import Template

async def jsu(request):
  return JSONResponse({'first':'resp', 'hello':'world', 'yay':'yuppie'})

async def nojsu(request):
  if request.POST:
    return Response('text/html', "<p style='color:#d3d3d3'>{}</p>".format(str(request.POST)))
  else:
    return Response('text/html', "<p style='color:#d3d3d3'>Getter</p>")
    
async def ep(request):
  if not request.GET:
    return Http404()
  else:
    q = await app.conn.fetch('select * from test_data where unique_id = %s' % request.GET['id'][0])
    return JSONResponse({'id':q[0][0], 'value': q[0][1]})

async def nm(request):
  t = Template('test.html')
  
  return t.render({'name':'suyash', 'name2':'gupta'})

urls = [
        ('/hello', jsu),
        ('/post', nojsu),
        ('/epp', ep),
        ('/nm', nm),
        ]

app = App(urls)
app.start_server()
