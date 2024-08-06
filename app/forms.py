from django import forms

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