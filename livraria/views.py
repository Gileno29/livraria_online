from django.shortcuts import render
import requests
import json
# Create your views here.
KEY_GOOGLE='AIzaSyAcbqEtwJ9dUexv8q5RoZXzuXGxCr40jME'


URL='https://www.googleapis.com/books/v1/volumes?q=terror+intitle:keyes&key='+KEY_GOOGLE

def index(request):
    
    response=requests.request("GET", URL)

    if response.status_code == 200:
        data = json.loads(response.content)
        dados={'dados': data['items']}
    return render(request, 'index.html', dados)


