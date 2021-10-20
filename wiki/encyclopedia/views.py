from django.shortcuts import render
from markdown import markdown
from django.http import HttpResponse
from django import forms
import random
from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 5}))
  
class EditPageForm(forms.Form):
    Title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'readonly':'readonly'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 5}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entri(request, title):
    content = util.get_entry(title)
    if content is None:
       return render(request, "encyclopedia/entri.html", {
              "content" :"Page not found, or not yet written"
              })

    else:
               return render(request, "encyclopedia/entri.html", {
               "content" :markdown(content), "title":title
               })


def add(request):
    entries_list = util.list_entries()
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title not in entries_list:
                util.save_entry(title, f"#{title} \n {content}")
                return entri(request, title)
            else:
                form.add_error('title', 'Error! An article with the same name already exists!')
                return render(request, "encyclopedia/add.html", {
                    "form": form
                })
    return render(request, "encyclopedia/add.html", {
        "form": NewPageForm()
    })


def edit(request, title):
    text = util.get_entry(title)
    if request.method == "POST":
        form = request.POST
        print(form)
        Text = form['text']
        text = markdown(Text)
        util.save_entry(title, f"#{title} \n {text}")
        return entri(request, title)
    else:
        result = markdown(text)
        return render(request, "encyclopedia/edit.html", {
             "title": title,
             "text": result.split('</h1>')[1].replace("<p>",'').replace("</p>", '')
        })

def search(requests):
    enc_list = []
    if requests.method == "POST":
        form = requests.POST
    wiki_list = util.list_entries()
    wiki_list_lower = []
    for wiki in wiki_list:
        wiki_list_lower.append(wiki.lower())
    if form['q'].lower() in wiki_list_lower:
        return page(requests, form['q'])
    elif wiki in wiki_list:
        for wiki in wiki_list:
            wiki_lower = wiki.lower()
            if wiki_lower.find(form['q'].lower()) != -1:
                enc_list.append(wiki)
        return render(requests, "encyclopedia/search.html", {
            "contents": enc_list
        })

    else:
        return render(requests, "encyclopedia/search.html")

def random_page(request):
   return entri(request, random.choice(util.list_entries()))
   