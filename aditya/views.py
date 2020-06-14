
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    
    django_text = request.GET.get('text', 'default')

    
    checkbox_punc = request.GET.get('checkbox_punc', 'off')
    checkbox_upper = request.GET.get('checkbox_upper', 'off')
    checkbox_newline_remover = request.GET.get('checkbox_newline_remover', 'off')
    checkbox_extra_space_remover = request.GET.get('checkbox_extra_space_remover', 'off')

    
    if checkbox_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in django_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(checkbox_upper=="on"):
        analyzed = ""
        for char in django_text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
       
        return render(request, 'analyze.html', params)

    elif(checkbox_newline_remover =="on"):
        analyzed = ""
        for index, char in enumerate(django_text):
            if not(django_text[index] == " " and django_text[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)

    elif (checkbox_extra_space_remover == "on"):
        analyzed = ""
        for char in django_text:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

