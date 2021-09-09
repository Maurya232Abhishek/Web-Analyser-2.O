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
def completeText(data):#this function takes htmlcontent as input nd returns strings which contains all the text of the html content
    text=divsText(data)+headingsText(data)+paragraphsText(data)+altText(data)
    return text
def sentence(data):# this program takes html content as input and returns the list of the sentences
    text=completeText(data)
    sentences = st(text)
    return sentences
def words(data):#this program takes html content as input and returns the list of the words
    text=completeText(data)
    words=wt(text)
    return words
def wordswithfrequencies(data):#this function take words of list and produce the frquencies of all words
    text=words(data)
    wordswithfrequencies=nltk.FreqDist(text)
    Keyvaluepairs=wordswithfrequencies.items()
    return Keyvaluepairs
def stopwords():#this function all stopwords of english words
    stops= sw.words('english')
    return stops
def removestopwords(data):#this function remove all stopwords of given data(or input)
    text=completeText(data)
    stops=stopwords()
    tokens=wt(text)
    tokenscopy=tokens.copy()
    print(len(tokens))

    for token in tokenscopy:
        if token.lower() in stops:
            tokens.remove(token)
    return tokens


url = "https://varanasi-software-junction.business.site/"
text = removestopwords(dd.downloadUrl(url))
#text2 = words(dd.downloadUrl(url))



print(('this' in text))
print(len(text))

