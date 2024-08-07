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
