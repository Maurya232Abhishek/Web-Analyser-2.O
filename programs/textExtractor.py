import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords as sw
import htmlTag as ht
import downloader as dd
import urlExtractor as ue

def divsText(data):#This function takes input htmlcontent and strings of text inside divs
    divs = ht.getDivs(data)
    output = ""
    #print(divs[3].text)
    for i in divs:
        output += " "+i.text
    return output

def headingsText(data): #This function takes input htmlcontent and produces a string of text inside headings
    headings=ht.getHeadings(data) #It takes input htmlcontent give list of headings
    output=""
    for i in headings:
        output = output +" "+i.text
    return output
def paragraphsText(data): #This function takes input htmlcontent and produces a string of text inside pragraph tag
    paragraphs = ht.getParagraphs(data)
    output=""
    for i in paragraphs:
        output += " " + i.text
    return output
def altText(data):#This function takes input htmlcontent and url of website and produces a string alts
    alts = ht.getImageAlts(data)
    output=""
    for i in alts:
        if i==None:
            continue
        output += " , "+ str(i)
    return output
#def CompleteText(data):


#url = "https://varanasi-software-junction.business.site/"
#text = altText(dd.downloadUrl(url))
#print(text)