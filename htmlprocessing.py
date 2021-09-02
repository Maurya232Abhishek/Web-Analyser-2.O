import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup as bs
# intialize the set of links
#internal_urls = set()
#external_urls = set()

#def getHref(url):
#    return url.get("href")
def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    print(parsed)
    #print(type(parsed))
    return bool(parsed.netloc) and bool(parsed.scheme)
def getDomainName(url):
    #Get the domain name from an url
    return urlparse(url).netloc

url="https://www.geeksforgeeks.org/"

#print(is_valid(url))
#print(getDomainName(url))
#urls =set()
#domain_name = getDomainName(url)
urls = set()
domain_name=getDomainName(url)
htmlcontent = requests.get(url).content #requests.get(url).content :It downlaods html content
soup = bs(htmlcontent,"html.parser")# arranges Html content as it is written
temp=soup.findAll("a")# input is html tag and gives output searches all content of that tag
a_tag=temp[0]
print(a_tag)
dict = a_tag.attrs # converts atrribute of tag in form dictionary
href = dict.get("href") # href value
print(href)
#print(href)
#print(temp)
#print(len(temp))
href = urljoin(url,href)
print(href)
parsed_href= urlparse(href)
print(parsed_href)
href = parsed_href.scheme +"://"+parsed_href.netloc + parsed_href.path
print(href)