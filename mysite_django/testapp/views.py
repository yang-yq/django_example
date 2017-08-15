from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.
from testapp import models

def index(request):
    #return HttpResponse("hello world");
    return render(request,"index.html")

def insert(request):
    #return HttpResponse("hello world");
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password", None)
        models.Userinfo.objects.create(username=username,password=password)

    data = models.Userinfo.objects.all()
    return render(request,"show.html",{"data":data})
