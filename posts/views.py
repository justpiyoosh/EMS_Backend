from django.shortcuts import render
from django.http import HttpResponse , Http404 , JsonResponse

# Create your views here.

from .models import Post

def index(request , post_id  ,*args , **kwargs):
    data = {
            "id" : post_id ,    
        }
    try:
        obj = Post.objects.get(id = post_id)
        data["content"] = obj.content
        status = 200
    except:
        data["message"] = "Not Found"
        status = 404
    return JsonResponse(data,status = status)

def posts_list_view(request , *args  , **kwargs):
    all_posts = Post.objects.all()
    posts_list = [{"post_id" : post.id , "content" : post.content} for post in all_posts]
    data = {
        "response" : posts_list
    }
    return JsonResponse(data , status = 200)
