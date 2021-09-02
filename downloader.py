#Downloader
import pandas as pd
import requests
import urllib.request, urllib.error, urllib.parse
def getUrlContent(url):
    #Downloads and returns HTML content
    return requests.get(url).content
def SaveFile(filename,data):
    file = open(filename,"w")
    file.write(data)
    file.flush()
    file.close()
def getLocalFileName(site):
    filedirectory = "saved/"
    if site.startswith("https://"):
        filename = site.replace("https://", "") + ".txt"
        filename = filename.replace("/","-")
    else:
        filename = site.replace("http://", "") + ".txt"
    return filedirectory + filename