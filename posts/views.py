from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Post

def index(request , post_id  ,*args , **kwargs):
    obj = Post.objects.get(id = post_id)
    return HttpResponse(f"<h1>{post_id} - Post is : {obj.content} </h1>")
