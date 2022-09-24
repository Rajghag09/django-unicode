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

def query(request):
  if request.method == "GET":
    query = request.GET.get('username')
  
  if User.objects.filter(username=query).exists():
    data=User.objects.filter(username=query)
    full_name=data[0].name
    q=data[0]
    q.count=q.count+1
    q.save()
    
    context={
      'username':query,
      'full_name':full_name,
    }
    
    return render(request,'query.html',context)

  elif query==None:
    return render(request,'query.html')
  
  else:
    context={
      'username':'Username not found',
      'full_name':None,
    }

    return render(request,'query.html',context)
  
def top(request):
  data=User.objects.all().order_by('-count')

  context={
    'top1':data[0].username,
    'top2':data[1].username,
    'top3':data[2].username
  }

  return render(request,'top.html',context)


