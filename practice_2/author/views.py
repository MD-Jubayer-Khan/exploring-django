from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_author(req):
    if req.method == 'POST':
         author_form = forms.AuthorForm(req.POST)
         if author_form.is_valid():
              author_form.save()
              return redirect('add-author')
    else:
         author_form = forms.AuthorForm()
    return render(req, 'add_author.html', {'form':author_form})