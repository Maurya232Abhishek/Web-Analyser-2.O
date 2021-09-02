import downloaderPunit as dd


site = "https://timesofindia.indiatimes.com/tv/news/hindi/punit-pathak-on-his-engagement-still-digesting-the-fact-that-this-happened/articleshow/77779750.cms"

print(site)
htmlcontent = dd.getUrlContent(site)
htmlcontent = str(htmlcontent)
print(htmlcontent)
filename=dd.getLocalFileName(site)
dd.SaveFile(filename,htmlcontent)