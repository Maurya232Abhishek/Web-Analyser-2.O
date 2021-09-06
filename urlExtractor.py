import requests
import downloader as dd
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
    #print(parsed)
    #print((parsed))
    return bool(parsed.netloc) and bool(parsed.scheme)
def getDomainName(url):
    #Get the domain name from an url
    return urlparse(url).netloc
def get_all_website_links(url):

    internal_urls=set()
    external_urls=set()
    domain_name = getDomainName(url)
    htmlcontent =   dd.downloadUrl(url)# requests.get(url).content :It downlaods html content
    soup = bs(htmlcontent, "html.parser")  # arranges Html content as it is written
    for a_tag in soup.findAll("a"): #soup.findAll("a")# input is html tag and gives output searches all content of that tag
        dict = a_tag.attrs  # converts atrribute of tag in form dictionary
        href = dict.get("href")  # href value
        if href == "" or href is None:
            continue
        # joint the URL if it's relative
        href = urljoin(url,href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
                external_urls.add(href)
            continue

        internal_urls.add(href)
    return internal_urls,external_urls
url="https://www.geeksforgeeks.org/"

print(is_valid(url))
#print(getDomainName(url))
#urls =set()
#domain_name = getDomainName(url)

#internal,external=get_all_website_links(url)

#print(len(internal),internal)
#print(len(external),external)