from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.urls import reverse


task=["eat","sleep","work"]

class newtextform(forms.Form):
    tasks=forms.CharField(label="Add new Task")



def index(request):
    if request.method == "POST":
        form = newtextform(request.POST)

        if form.is_valid():
            tasks =form.cleaned_data["tasks"]
            task.append(tasks)
            return HttpResponseRedirect(reverse("app:index"))



    return render(request,"app/index.html",{
        "tasks":task,
        "form":newtextform(),

     })



# Create your views here.
