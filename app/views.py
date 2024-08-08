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


# insert topic by using model forms...

def insert_topic_by_modelforms(request):
    d={'ETMFO':TopicModelForm()}
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()

            return HttpResponse('topic incerted')

    return render(request,'insert_topic_by_modelforms.html',d)

#insert into webpage by using forms..

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
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
            WO.save()

            return HttpResponse('webpage is created')

    return render(request,'insert_webpage.html',d)



#insert into webpage using modelforms...

def insert_webpage_by_MF(request):
    EWMFO=WebpageModelForm()
    d={'EWMFO':EWMFO}

    if request.method=='POST':
        WMFDO=WebpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()

            return HttpResponse('webpage is created')

    return render(request,'insert_webpage_by_MF.html',d)


#insert into accessrecords using modelforms...

def insert_accessrecords_by_MF(request):
    d={'EARMFO':AccessRecordsModelForm()}

    if request.method=='POST':
        ARMFDO=AccessRecordsModelForm(request.POST)
        if ARMFDO.is_valid():
            ARMFDO.save()

            return HttpResponse('accessrecord is created')
        
    return render(request,'insert_accessrecords_by_MF.html',d)
