from django.http import HttpResponse
from django.shortcuts import render
import downloader as dd
def index(request):
    url=""
    foldername=""
    htmlcontent=""
    if request.GET:
        url= request.GET["url"]
        foldername = request.GET["foldername"]
        htmlcontent = dd.downloadUrl(url)
    data={"url":url,"foldername":foldername,"htmlcontent":htmlcontent   }
    return render(request,"page.html",{"data":data})