import downloader as dd
import  filehandling as fh
from bs4 import BeautifulSoup as bs

site = "http://bhuonline.in/"

print(site)
htmlcontent = dd.getUrlContent(site)
htmlcontent = str(htmlcontent)
print(htmlcontent)
filename=bs.getLocalFileName(site)
bs.SaveFile(filename,htmlcontent)