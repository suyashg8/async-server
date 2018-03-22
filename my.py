from main import App
from responses import JSONResponse, Response
from responses import Http404
from templates import Template

def jsu(request):
  return JSONResponse({'first':'resp', 'hello':'world', 'yay':'yuppie'})

def nojsu(request):
  if request.POST:
    return Response('text/html', "<p style='color:#d3d3d3'>{}</p>".format(str(request.POST)))
  else:
    return Response('text/html', "<p style='color:#d3d3d3'>Getter</p>")
    
def ep(request):
  if not request.GET:
    return Http404()
  else:
    with app.conn.cursor() as cur:
      cur.execute('select * from test_data where id = %s' % request.GET['id'][0])
      q = cur.fetchall()
      return JSONResponse({'id':q[0][0], 'value': q[0][1]})

def nm(request):
  t = Template('test.html')
  
  return t.render({'name':'suyash', 'name2':'gupta'})

urls = [
        ('/hello', jsu),
        ('/post', nojsu),
        ('/ep', ep),
        ('/nm', nm),
        ]

app = App(urls)
app.init_db('async_test_db')
app.start_server()
