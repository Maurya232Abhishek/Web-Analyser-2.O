def SaveFile (filename, data):

    file = open(filename,"w")
    file.write(data)
    file.flush()
    file.close()
def getLocalFileName(site):
    filedirectory="saved/"
    if site.startswith("https://"):


        filename = site.replace("https://","") + ".txt"
        filename = filename.replace("/","-")

    else:
        filename = site.replace("http://","") + ".txt"
        filename = filename.replace("/", "-")

    return filedirectory + filename
def getLocalPicName(site):
    filedirectory="saved/"
    if site.startswith("https://"):


        filename = site.replace("https://","") + ".PNG"
        filename = filename.replace("/","-")

    else:
        filename = site.replace("http://","") + ".PNG"
        filename = filename.replace("/", "-")

    return filedirectory + filename
def SaveBinaryFile(filename,data): #forimage
    file=open(filename,"wb")
    file.write(data)
    file.flush()
    file.close()