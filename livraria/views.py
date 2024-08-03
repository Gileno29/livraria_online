from django.shortcuts import render, redirect
import requests
import json
# Create your views here.
KEY_GOOGLE='AIzaSyAcbqEtwJ9dUexv8q5RoZXzuXGxCr40jME'

URL_BASE='https://www.googleapis.com/books/v1/volumes/?q='
#URL="https://www.googleapis.com/books/v1/volumes?q='':keyes&key="+KEY_GOOGLE

def getResponse(url):
   url=url+":keyes&key="+KEY_GOOGLE
   response=requests.request("GET", url)
   print("Minha URL: ", url)
   if response.status_code == 200:
        data = json.loads(response.content) 
        return data['items']
   return None

def index(request):
    dados=request.session.get('dados')
    
    if dados:
         return render(request, 'index.html', dados)
    data = getResponse(URL_BASE)

    if data != None:
        dados={'dados': data}
    return render(request, 'index.html', dados)


def details(request, id):

    data=getResponse(URL_BASE+str(id))
    dados={'dados': data}
   
    return render(request, 'detalhes.html', dados)


def find(request):
    if request.POST:
        tipo= request.POST.get('tipoSelecao')
        print("meu tipo de selecao", tipo)
        if int(tipo)==1:
            url_busca=URL_BASE+'subject:'+'+'+request.POST.get('filtro')
            data=getResponse(url_busca)
            dados={'dados': data}
            request.session['dados'] = dados
            return redirect('/')
        
        if int(tipo)==2:
            url_busca= URL_BASE+'inauthor:'+'+'+request.POST.get('filtro')
            data=getResponse(url_busca)
            dados={'dados': data}
            request.session['dados'] = dados
            return redirect('/')
        

    return redirect('/')