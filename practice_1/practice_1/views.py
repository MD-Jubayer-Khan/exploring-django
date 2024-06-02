from django.shortcuts import render
from posts.models import Post
from author.models import Author

def home(req):
    data = Post.objects.all()
    data2 = Author.objects.all()
    return render(req, 'index.html', {'data':data, 'data2': data2})