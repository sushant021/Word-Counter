from django.shortcuts import render
import operator
from nscounter.forms import mainForm


def index(request):
	form = mainForm()
	return render(request, 'index.html',{'form':form})

def counterpage(request):
	if request.method == 'POST':
		form= mainForm(request.POST)
		if form.is_valid():
			textBlock=form.cleaned_data['maintext']
			searchWord=form.cleaned_data['searchword']
		wordDict= {}
		searchWordDict= {}

		words = textBlock.split()
		for word in words:
			if word in wordDict:
				wordDict[word] +=1
			else:
				wordDict[word] =1
		sortedWords = sorted(wordDict.items(),key=operator.itemgetter(1),reverse=True)

		for word in words:
			if word in searchWordDict:
				searchWordDict[word]+=1
			elif word==searchWord:
				searchWordDict[word] = 1
		searchWordList=searchWordDict.items()
		print (searchWordDict)
		print (searchWordList)
		#searchWordList= searchWordDict.items()
		return render (request,'counterpage.html',{'no_of_words':len(words),'searchWord':searchWord,'sortedWords':sortedWords,'searchWordList':searchWordList})


    
    
  