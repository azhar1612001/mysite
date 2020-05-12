#i have created file -Azhar
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    pras={'name':'azhar','character':'good'}
    return render(request,"index2.html")
def about(request):
    djtext=request.POST.get('name','name')
    removepunc=request.POST.get('removepunc','off')
    captilise=request.POST.get('captilise','off')
    newlineremover=request.POST.get('newline','off')
    space=request.POST.get('space','off')
    if removepunc=='on':
        Puntuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analysed=''
        for char in djtext:
            if char not in Puntuation:
                analysed=analysed + char
        djtext=analysed
        params={'purpose':'Remove Puntuation','analysed_text':analysed}
    if captilise=='on':
        analysed=djtext.upper()
        params={'purpose':'Captilise All','analysed_text':analysed}
        djtext=analysed
    if newlineremover=='on':
        analysed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analysed=analysed + char
            if char==' ':
                analysed=analysed+char
        params={'purpose':'Remove New Line','analysed_text':analysed}
        djtext=analysed
    if space=='on':
        analysed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analysed=analysed+char
        params={'purpose':'Extra Space Remover','analysed_text':analysed}
        djtext=analysed
    if removepunc=='on' or captilise=='on' or newlineremover=='on' or space=='on':
        return render(request,'analyse2.html',params)
    else:
        return HttpResponse("Please select atleast one operation")
