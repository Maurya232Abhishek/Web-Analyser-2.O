import downloader as dd

site = "https://opportunities.rbi.org.in/"
print(site)
htmlcontent = dd.getUrlContent(site)
htmlcontent = str(htmlcontent)
print(htmlcontent)
filename=dd.getLocalFileName(site)
dd.SaveFile(filename,htmlcontent)