from django import forms
from app.models import *

c=[('Male','male'),('Female','female')]
s=[('Python','python'),('Sql','sql')]
class StudentForm(forms.Form):
    sname=forms.CharField(max_length=50)
    sage=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    gender=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    subjects=forms.MultipleChoiceField(choices=s,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':5}))


class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=100)


class TopicModelForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'


class WebpageForm(forms.Form):
    topicname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()


class WebpageModelForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'



class AccessRecordsModelForm(forms.ModelForm):
    class Meta():
        model=AccessRecords
        fields='__all__'