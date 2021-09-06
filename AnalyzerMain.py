import downloader as dd
import  filehandling as fh

import urlExtractor as ue

def downloadAndSave(site): # it downloads only html content of the given link
    htmlcontent = dd.getUrlContent(site)
    htmlcontent = str(htmlcontent)
    filename=fh.getLocalFileName(site)
    fh.SaveFile(filename,htmlcontent)
def downloadAndSaveUrlLinkdata(site):# it downloads htmlcontent of the given link as well as html content of urls present in the Htmlcontent
    htmlcontent = dd.getUrlContent(site)
    htmlcontent = str(htmlcontent)
    internal_urls,external_urls = ue.get_all_website_links(site)
    print(len(internal_urls),len(external_urls))
    for i in internal_urls:
        htmlcontent += " "+str(dd.getUrlContent(i))
#    for i in external_urls:
#        htmlcontent += " "+str(dd.getUrlContent(i))
    filename=fh.getLocalFileName(site)
    fh.SaveFile(filename,htmlcontent)
site="https://varanasisoftwarejunction.blogspot.com/2021/02/how-to-create-site-using-django.html"
data=dd.downloadUrl(site)
downloadAndSaveUrlLinkdata(site)
print(data)


