from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordDICT = {}
    for word in wordlist:
        if word in wordDICT:
            #Increase
            wordDICT[word] +=1
        else:
            #add to dict
            wordDICT[word] = 1
    sortedWords = sorted(wordDICT.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedWord':sortedWords})
