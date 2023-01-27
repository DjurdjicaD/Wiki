from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.shortcuts import render
import markdown2
import random

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def addNewPage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
        else:
            return render(request, "encyclopedia/index.html", {
                "form":form
            })
    return render(request, "encyclopedia/addNewPage.html",{
        "form": NewPageForm()
    })

def getPage(request):
    title = request.GET.get("title")
    content = util.get_entry(title)
    if content == None:
        content = markdown2.markdown(f'## {title}\'s page has not been found')
    else:
        content = markdown2.markdown(content)
    return render(request, "encyclopedia/page.html", {
        "title":content
    })

def getRandomPage(request):
    items = util.list_entries()
    item = random.choice(items)
    content = util.get_entry(item)
    contentHTML = markdown2.markdown(content)
    return render(request, "encyclopedia/page.html",{
        "title":contentHTML
    })



