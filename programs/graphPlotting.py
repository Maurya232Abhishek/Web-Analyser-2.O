import nltk
import matplotlib.pyplot as plt
import textExtractor as te
import downloader as dd
import trainingSet as t
def Gplot(data):
#this function take words and their frequencies and produce the  plot of  a graph(curve)
    word=te.words(data)
    text=nltk.FreqDist(word)
   # print(text.values())
   # print(text.keys())
    n=len(text)
    pllt=text.plot(n,cumulative=False)
    return pllt
def SaveGplot(data):
#this function take figure(graph) and save graph in internal storage
    fig = plt.figure()
    Gplot(data)
    plt.show()
    fig.savefig("F:\Web-Analyser-2.O\programs\saved\Graph/Gplot.png")
    return fig
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
    fig.savefig("F:\Web-Analyser-2.O\programs\saved\Graph/Rplot.png")
    return fig
def interplot(data):
#this function produce graph between frequency and words of intersections of two sets
    dict=te.frequincyOfIntersectionsSet(data)
    text=nltk.FreqDist(dict)
    n=len(text)
    pltt=text.plot(n,cumulative=False)
    return pltt

def Saveinterplot(data):
#this function take figure(graph) from interplot and save graph in internal storage
    fig=plt.figure()
    interplot(data)
    plt.show()
    fig.savefig("F:\Web-Analyser-2.O\programs\saved\Graph/interplot.png")
    return fig

def getFullData(data,trainingset):
#this intersections list and corresponding frequincy list
    mainset=te.getSet(data)
    m=mainset.intersection(trainingset)
    l=list(m)
    text=te.dict1(data)
    words=[]
    frequiencies=[]
    for word in l:
        words.append(word)
        frequiencies.append(text[word])
    return words,frequiencies

def getFullplot(data,trainingSet):
    lst=getFullData(data,trainingSet)
    w=lst[0]
    f=lst[1]
    res={w[i]:f[i] for i in range(len(w))}
    text=nltk.FreqDist(res)
    n=len(text)
    pltt=text.plot(n,cumulative=False)
    return pltt

def getSaveFullplot(data,trainingSet):
#this function take figure (graph) from interplot and save graph in internal storage
    newfig=plt.figure()
    getFullplot(data,trainingSet)
    plt.show()
    newfig.savefig("F:\Web-Analyser-2.O\programs\saved\Graph/Fullplot.png")
    return newfig

url= "https://www.geeksforgeeks.org/"
data = dd.downloadUrl(url)
print(getSaveFullplot(data,t.training()))
