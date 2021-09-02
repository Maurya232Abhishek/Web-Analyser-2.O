import downloader as dd
import  filehandling as fh

def downlaodAndSave(site):
    htmlcontent = dd.getUrlContent(site)
    htmlcontent = str(htmlcontent)
    filename=fh.getLocalFileName(site)
    fh.SaveFile(filename,htmlcontent)


