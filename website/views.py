from django.db.models.fields import FilePathField
from django.shortcuts import render
from .models import *

import requests
from bs4 import BeautifulSoup
# Create your views here.


def index(request):
    intro = Intro.objects.all()
    coding = Coding_skils.objects.all()
    education = Education_experience.objects.all()
    featured = Fetured_Work.objects.all()
    certificate = Certificate.objects.all()

    # data scraped from wordpress blog
    r = requests.get("https://simplykarthic.wordpress.com/")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    a = soup.find_all("h2", {"class": "entry-title"})
    b = soup.find_all("p", {"class": None, "id": None})
    c = soup.find_all("time", {"class": "entry-date"})
    Recent_title = []
    Recent_des = []
    Recent_date = []
    for text in a:
        temp = text.find_all("a")[0].text
        Recent_title.append(temp)
    for dess in b:
        tempr = dess.text
        Recent_des.append(tempr)
    for datt in c:
        tempre = datt.text
        Recent_date.append(tempre)

    recent = []
    name = "blog"
    for age in range(4):
        data = "%s%d" % (name, age)
        data = Blog()
        data.title = Recent_title[age]
        data.des = Recent_des[age]
        data.dat = Recent_date[age]
        recent.append(data)

    return render(request, 'index.html', {'intro': intro, 'coding': coding, 'education': education, 'featured': featured, 'certificate': certificate, 'recent': recent})


def blog(request):

    return render(request, 'blog.html')


def portfolio(request):

    return render(request, 'portfolio.html')
