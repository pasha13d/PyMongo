from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    #print(request)
    #print(dir(request))
    #print(request.method)
    return HttpResponse("<!DOCTYPE html><html><head><style>h1{color: green;}</style></head><body></body></html><h1>Hello World</h1>")

# def home(request):
#     response = HttpResponse(content_type='application/json')
#     response.content = '<!DOCTYPE html><html><head><style>h1{color: green;}</style></head><body></body></html><h1>Hello World</h1>'
#     #print(dir(response))
#     response.write("<p>Here's the text of the web page.</p>")

#     return response

def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path")