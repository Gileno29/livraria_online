from django.shortcuts import render, redirect
import requests
import json
from . import models
# Create your views here.
KEY_GOOGLE='AIzaSyAcbqEtwJ9dUexv8q5RoZXzuXGxCr40jME'

URL_BASE='https://www.googleapis.com/books/v1/volumes/?q='
#URL="https://www.googleapis.com/books/v1/volumes?q='':keyes&key="+KEY_GOOGLE

def getResponse(url):
   url=url+"&key="+KEY_GOOGLE
   response=requests.request("GET", url)
   print("Minha URL: ", url)
   if response.status_code == 200:
        data = json.loads(response.content) 
        
        if data['totalItems']!=0:
            return data['items']
        else:
            return None
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
            url_busca=URL_BASE+'+'+'subject:'+request.POST.get('filtro')
            data=getResponse(url_busca)
            dados={'dados': data}
            request.session['dados'] = dados
            return redirect('/')
        
        if int(tipo)==2:
            url_busca= URL_BASE+'+'+'inauthor:'+request.POST.get('filtro')
            data=getResponse(url_busca)
            dados={'dados': data}
            request.session['dados'] = dados
            return redirect('/')
        
        if int(tipo)==3:
            url_busca= URL_BASE+'+'+'intitle:'+request.POST.get('filtro')
            data=getResponse(url_busca)
            dados={'dados': data}
            request.session['dados'] = dados
            return redirect('/')


    return redirect('/')


def addCarrinho(request, id):
    c=models.Carrinho()
    c.item=id
    c.save()

    return redirect('/')

def verCarrinho(request):
    dados=[]
    itens= models.Carrinho.objects.filter(comprado=False)
    for i in itens:
        dados.append(getResponse(URL_BASE+str(i.item)))
   
    produtos=[]
    for i in dados:

        produto={'titulo':i[0]['volumeInfo']['title'],
                          'categorias':i[0]['volumeInfo']['categories'],
                          'imagem':i[0]['volumeInfo']['imageLinks']['thumbnail']  }
        
        produtos.append(produto)
    
    
   # print(produtos)
    produtos={'produtos':produtos}
    return render(request,'carrinho.html' , produtos )