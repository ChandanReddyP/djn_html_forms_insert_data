from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def djforms(request):
    ESTFO=StudentForm()
    d={'ESTFO':ESTFO}
    return render(request,'djforms.html',d)