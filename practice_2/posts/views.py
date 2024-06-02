from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.
def add_album(req):
    if req.method == 'POST':
         post_form = forms.PostForm(req.POST)
         if post_form.is_valid():
              post_form.save()
              return redirect('home')
    else:
         post_form = forms.PostForm()
    return render(req, 'add_post.html', {'form':post_form})

def edit_album(req, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm( instance = post)
    if req.method == 'POST':
         post_form = forms.PostForm(req.POST, instance= post)
         if post_form.is_valid():
              post_form.save()
              return redirect('home')

    return render(req, 'add_post.html', {'form':post_form})

def delete_album(req, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')