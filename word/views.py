from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import random

def home(request):    
    r = requests.get('https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt').content
    r=str(r)
    x=r.split('\\n')
    j=random.choice(x)
    return render(request,"home.html",{'random':j,'options':r})
    