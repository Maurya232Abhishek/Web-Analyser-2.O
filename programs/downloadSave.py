import downloader as dd
import  filehandling as fh
import urlExtractor as ue
import htmlTag as ht

def downloadAndSave(site): # it downloads only html content of the given link
    htmlcontent = dd.getUrlContent(site)
    htmlcontent = str(htmlcontent)
    filename=fh.getLocalFileName(site)
    fh.SaveFile(filename,htmlcontent)
def downloadAndSaveUrlLinkData(site):# it downloads htmlcontent of the given link as well as html content of urls present in the Htmlcontent

    internal_urls,external_urls = ue.get_all_website_links(site)
    #print(len(internal_urls),len(external_urls))
    for i in internal_urls:
        htmlcontent = str(dd.getUrlContent(i))
        filename = fh.getLocalFileName(i)
        fh.SaveFile(filename, htmlcontent)
#    for i in external_urls:
#        htmlcontent += " "+str(dd.getUrlContent(i))
def saveImageFromUrlToFile(imageurl,filename):
    data=dd.getUrlContent(imageurl)
    fh.SaveBinaryFile(filename,data)
def download_all_images(htmlcontent,siteurl):
    urls = ht.getImageUrls(htmlcontent,siteurl)
    for url in urls:
        saveImageFromUrlToFile(url,fh.getLocalPicName(url))



site="https://varanasi-software-junction.business.site/"
#downloadAndSaveUrlLinkData(site)
#SaveImageFromUrlToFile("https://media.istockphoto.com/photos/colorful-sunset-scenery-on-open-field-picture-id1216579927?s=612x612","manjit")
download_all_images(dd.downloadUrl(site),site)

