from django.http import HttpResponse
from . import task1

# Create your views here.
def index(request):
  return HttpResponse("Home")

def task2(request,a,b):
  mydict = str(task1.True_False(a,b))
  return HttpResponse(mydict)
