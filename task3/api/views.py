from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import User

def index(request):
  return HttpResponse("Home")

def api(request):
  if request.method == "GET":
    info = request.GET.get('username')

  if info != None:
    url = "https://instagram130.p.rapidapi.com/account-info"

    querystring = {"username":info}

    headers = {
	    "X-RapidAPI-Key": "ca27c07d86mshba1e8019cc353e4p13d313jsn24c3de20e7c5",
      "X-RapidAPI-Host": "instagram130.p.rapidapi.com"
      }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
     
    context={
        'full_name':response['full_name'],
        'biography':response['biography']
      }

    if User.objects.filter(username=info).exists():
      pass

    else:
      q=User(username=info,name=response['full_name'],bio=response['biography'])
      q.save()


    return render(request,'index.html',context)

  else:
    return render(request,'index.html')

