from django.shortcuts import render
from django.http import HttpResponse , Http404 , JsonResponse
import json



#for pdf
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas




from .models import Post

def index(request , *args , **kwargs):
    # if request.method == "GET":
    #     return HttpResponse('<h1>Welcome on Homepage</h1>')
    # else:
    #     data = {"message" : "only get method is allowed"}
    #     return JsonResponse(data)
    return HttpResponse("<h1>Welcome on EMS Homepage!!</h1>")

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
    if "session-id" not in request.headers:
        return JsonResponse({"message" : "unauthorized"}) 
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


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

    
