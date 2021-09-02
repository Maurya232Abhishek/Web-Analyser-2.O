import downloader as dd
import  filehandling as fh

site = "https://www.rbi.org.in/home"

print(site)
htmlcontent = dd.getUrlContent(site)
htmlcontent = str(htmlcontent)
print(htmlcontent)
filename=fh.getLocalFileName(site)
fh.SaveFile(filename,htmlcontent)