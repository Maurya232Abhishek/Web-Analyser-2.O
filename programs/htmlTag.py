from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup as bs
import urlExtractor as ue
import downloader as dd
def getDivs(htmlcontent): # takes input html content
    scraper = bs(htmlcontent,"html.parser")
    divs = scraper.find_all("div")
    divisions = []
    #print(type(divs))
    for div in divs:
        divisions.append(div)
    return divisions
def getHeadings(htmlcontent,h):# it takes two input htmlcontent and heading type h1 h2 or h3
    scraper = bs(htmlcontent,"html.parser")
    h1s=scraper.find_all(h)
    headings=[]

    for h1 in h1s:
        headings.append(h1)
    return headings
def getParagraphs(htmlcontent):
    scraper = bs(htmlcontent,"html.parser")
    ps = scraper.find_all("p")
    paragraphs=[]
    for p in ps:
        paragraphs.append(p)
    return ps
def getImages(htmlcontent,siteUrl):
    domain = ue.getDomainName(siteUrl)
    http = ue.urlparse(siteUrl).scheme
    siteurl = http + "://" +domain
    scraper = bs(htmlcontent, 'html.parser')
    imgs= scraper.find_all("img")
    imgurls=[]
    imgalts=[]
    for img in imgs:
        src= img.get('src')
        alt= img.get('alt')
        newurl=urljoin(siteurl,src)
        imgurls.append(newurl)
        imgalts.append(alt)
    return imgurls, imgalts


url="https://varanasi-software-junction.business.site/"

#div=getParagraphs(dd.downloadUrl(url))
#print((div))
urls,alts=getImages(dd.downloadUrl(url),url)
print(urls)
print(alts)

def getImageSave(htmlcontent,url):