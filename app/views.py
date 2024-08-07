from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.


def djforms(request):
    
    ESTFO=StudentForm()
    d={'ESTFO':ESTFO}

    return render(request,'djforms.html',d)


def insert_topic(request):

    EFTO=TopicForm()
    d={'EFTO':EFTO}

    if request.method=='POST':
        FTDO=TopicForm(request.POST)
        if FTDO.is_valid():
            tn=FTDO.cleaned_data['topicname']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is created')

    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    EFWO=WebpageForm()
    d={'EFWO':EFWO}

    if request.method=='POST':
        FWDO=WebpageForm(request.POST)
        if FWDO.is_valid():
            tn=FWDO.cleaned_data['topicname']
            na=FWDO.cleaned_data['name']
            ur=FWDO.cleaned_data['url']
            em=FWDO.cleaned_data['email']

            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topi_name=TO,name=na,url=ur,email=em)[0]
            WO.save()

            return HttpResponse('webpage is created')

    return render(request,'insert_webpage.html',d)