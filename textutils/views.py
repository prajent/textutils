# i have created this file - prajent shahi
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text', 'default')
    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose' : 'removed punctuation', 'analyzed_text':analyzed}
        #Analyze the text
        
        djtext = analyzed
    
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params= {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        


    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params= {'purpose': 'remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
        
    
    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        
        params= {'purpose': 'remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
        
    
    if(charcount=="on"):
        count=0 
        for char in djtext:
            count = count+1       

        params= {'purpose': 'charcter count', 'analyzed_text': count}
        djtext = analyzed
        

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover !="on" and newlineremover != "on"  and charcount != "on"):
        return HttpResponse("please select any operation")

    
    return render(request, 'analyze.html', params)

# def removepunc(request):
#     #Get the text
#     djtext=request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punctuations")

# def capfirst(request):
#     return HttpResponse("caption first")

# def newlineremove(request):
#     return HttpResponse("newline remover")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount")