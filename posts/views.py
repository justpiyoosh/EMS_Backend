from django.shortcuts import render
from django.http import HttpResponse , Http404 , JsonResponse
import json


from .models import Post

def index(request , *args , **kwargs):
    if request.method == "GET":
        return HttpResponse('<h1>Welcome on Homepage</h1>')
    else:
        data = {"message" : "only get method is allowed"}
        return JsonResponse(data)

def create_post(request , *args , **kwargs):
    if request.method == "POST":
        data = json.loads(request.body) #converts json to dictionary
        Post.objects.create(content=data['content'])
        return JsonResponse({"message" : "Post Created Successfully" })

def get_post(request , post_id  ,*args , **kwargs):
    if "session-id" not in request.headers:
        return JsonResponse({"message" : "unauthorized"}) 

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
    data["status"] = status
    return JsonResponse(data)


def get_all_posts(request , *args  , **kwargs):
    if request.method == "GET":
        all_posts = Post.objects.all()
        posts_list = [{"post_id" : post.id , "content" : post.content} for post in all_posts]
        data = {
            "response" : posts_list,
            "status" : 200
        }
        return JsonResponse(data)
    else: 
         return JsonResponse({"message" : "Only get method is allowed"})



def delete_post(request , post_id , *args , **kwargs):
    qs = Post.objects.filter(id = post_id)
    return JsonResponse({"message" : "Post deleted successfully"} , status=200)

    
