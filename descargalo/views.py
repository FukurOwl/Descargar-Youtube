import pafy
import youtube_dl
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')




def descargar(request):
    url = request.POST.get('link','')
    video = pafy.new(url)
    best = video.getbest()
    path = '/Descargas'
    best.download()
    return render(request, 'index.html')



