import nltk
import matplotlib.pyplot as plt
import textExtractor as te
import downloader as dd
def Rplot(data):
#this function plot the graph between frequencies and words(after removal stop words)
    words=te.removeStopWords(data)
    text=nltk.FreqDist(words)
    #print(text.values())
    #print(text.keys())
    #print(text.items())
    n=len(text)
    pltt=text.plot(n,cumulative=False)
    return pltt
def SaveRplot(data):
#this function take figure(graph) from Rplot and save graph in internal storage
    fig=plt.figure()
    Rplot(data)
    plt.show()
    fig.savefig("saved/Graph/SaveRpot.png")
    return fig
def getSet(data):
#this function convert the words(after removel of stop words) into set of given data(or input)
    words=te.removeStopWords(data)
    text=nltk.FreqDist(words)
    n=text.keys()
   # print(n)
    s1=set()
    for x in n:
        s1.add(x)
    return s1


url= "https://varanasi-software-junction.business.site/"
data = dd.downloadUrl(url)
print(getSet(data))

