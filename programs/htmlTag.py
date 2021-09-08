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
def getHeadings(htmlcontent):# it takes two input htmlcontent and heading type h1 h2 or h3
    scraper = bs(htmlcontent,"html.parser")
    h1s=scraper.find_all("h1")
    h2s=scraper.find_all("h2")
    h3s=scraper.find_all("h3")
    h4s=scraper.find_all("h4")
    h5s=scraper.find_all("h5")
    h6s=scraper.find_all("h6")
    headings=[]
    for h1 in h1s:
        headings.append(h1)
    for h2 in h2s:
        headings.append(h2)
    for h3 in h3s:
        headings.append(h3)
    for h4 in h4s:
        headings.append(h4)
    for h5 in h5s:
        headings.append(h5)
    for h6 in h6s:
        headings.append(h6)

    return headings
def getParagraphs(htmlcontent):
    scraper = bs(htmlcontent,"html.parser")
    ps = scraper.find_all("p")
    paragraphs=[]
    for p in ps:
        paragraphs.append(p)
    return ps
def getImageUrls(htmlcontent,siteUrl): # it givs list of images url and their alt values
    domain = ue.getDomainName(siteUrl)
    http = urlparse(siteUrl).scheme
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
    return imgurls
def getImageAlts(htmlcontent): # it givs list of images url and their alt values
    scraper = bs(htmlcontent, 'html.parser')
    imgs= scraper.find_all("img")
    imgalts=[]
    for img in imgs:
        alt= img.get('alt')
        imgalts.append(alt)
    return imgalts


url="https://varanasi-software-junction.business.site/"

#div=getHeadings(dd.downloadUrl(url))
#print((div))
#urls,alts=getImages(dd.downloadUrl(url),url)
#print(urls)
#print(alts)
#htmlcontent=dd.downloadUrl(url)
#print(htmlcontent)
#print(htmlcontent.find_all("div"))
#html = bs(htmlcontent,"html.parser")
#print(html.find_all("img"))
#print(html)
