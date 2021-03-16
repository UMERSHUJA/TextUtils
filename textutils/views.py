from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'Home/index.html')


def analyze(request):
    # GET the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    capitalized = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>.?/@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        context = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }
        
        analyzed = djtext

    if capitalized == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        context = {
            'purpose': 'Capitalize text',
            'analyzed_text': analyzed
        }
        analyzed = djtext


    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        context = {
            'purpose': 'New LineRemover',
            'analyzed_text': analyzed
        }
        analyzed = djtext


    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index] == '  '):
                analyzed = analyzed + char

        context = {
            'purpose': 'Extra Space Remover',
            'analyzed_text': analyzed
        }
        analyzed = djtext


    if charcounter == 'on':
        analyzed = 0
        for char in djtext:
            if char != ' ' or char != '.':
                analyzed = analyzed + 1


        context = {
            'purpose': 'Character Counter',
            'analyzed_text': "your paragraph has " + str(analyzed) + " characters." 
        }
    
    if removepunc != 'on' and charcounter != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and capitalize != 'on':
        return HttpResponse("Please select any of these operation.")


    return render(request, 'Home/analyze.html', context)


