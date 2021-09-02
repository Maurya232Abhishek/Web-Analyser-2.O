#Downloader
import pandas as pd
import requests
import urllib.request, urllib.error, urllib.parse
def getUrlContent(url):
    #Downloads and returns HTML content
    return requests.get(url).content

def downloadUrl(url):#need to be logined to the website
    #Downloads and returns content
    response = urllib.request.urlopen(url)
    webContent = response.read()
    return webContent

def getWebData(url):
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
    return d


#url="https://geeksforgeeks.com/"
#data =str(downloadUrl(url))

#fileName=urlf + ".txt"
#SaveFile(fileName,data)
#print(downloadUrl(url))
#print(getUrlContent(url))
#a="abhis.txt"
#b=".txt"
#print(a-b)
#print(getWebData(url))
