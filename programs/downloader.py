#Downloader
#import pandas as pd
import requests
import urllib.request, urllib.error, urllib.parse
def getUrlContent(url):
    #Downloads and returns content
    try:
        htmlcontent=requests.get(url).content
    except:
        htmlcontent= "NoData"
    finally:
        return htmlcontent

def downloadUrl(url):
    #Downloads and returns content
    try:
        response = urllib.request.urlopen(url)
        webContent = response.read()
    except:
        webContent = "NoData"
    return webContent



'''def getWebData(url):
    # if the Html data of given url is in CSV file then it shows the stored Html data
     #else it downloads the html content from internet and stores html data in CSV file and return the same
    data = pd.read_csv("urldata.csv")
    print(data)
    Url = list(data["Url"])
    #print(type(Url))
    #print(url not in Url)
    if url not in Url:
        n = len(data)
        d = str(getUrlContent(url))
        newrow = {"Fileno": n + 1, "Url": url, "Data": d}
        data = data.append(newrow, ignore_index=True)
        data.to_csv("urldata.csv", index=False)
    else:
        query = data[data["Url"] == url]
        d = query["Data"]
    return d'''
"""url="dpL00/"
data = getUrlContent(url)
print(data)
data2 = downloadUrl(url)
print(data2)"""
url="https://lh3.googleusercontent.com/p/AF1QipMmODRWLl_DXyr3YbwMbvCgTEAk6gak7HcQkxim=w600-h0"
#SaveImageFromUrlToFile(url,fil)