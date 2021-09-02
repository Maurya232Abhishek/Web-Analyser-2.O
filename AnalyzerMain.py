import downloader as dd

site = "https://www.rbi.org.in/home"
print(site)
htmlcontent = dd.getUrlContent(site)
htmlcontent = str(htmlcontent)
print(htmlcontent)
filename=dd.getLocalFileName(site)
dd.SaveFile(filename,htmlcontent)