from django.shortcuts import render
from django .http import HttpResponse
import bs4
import requests
# Create your views here.

def home(request):
    #return HttpResponse('<h1> Hello, from home </h1>')
    # names=['anu','anom','sunil']

    # d={
    #     'name': names,
    #     'college':'sxc'
    # }

    page=requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup=bs4.BeautifulSoup(page.content,'html.parser')
    num=1
    li=soup.findAll('li')
    names=[]
    for each in li:
        names.append(each.find('a').string)
        num+1
    d = {
        'names':names
    }

    return render(request,'home.html', d)

def bootcamp(camp):
    return HttpResponse('Hello from bootcamp')