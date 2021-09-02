import downloader as dd
site="https://geeksforgeeks.com"
print(site)
htmlcontent =  dd.getUrlContent(site)
htmlcontent = str(htmlcontent)
print(htmlcontent)
filename = dd.getLocalFileName(site)
dd.saveFile(filename,htmlcontent)
