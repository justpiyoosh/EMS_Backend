from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes ,authentication_classes
from rest_framework.permissions import IsAuthenticated


from account.models import Account
from blog.models import BlogPost
from blog.api.serializers import BlogPostSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
# @authentication_classes([])
def api_detail_blog_view(request, blog_id):

	try:
		blog_post = BlogPost.objects.get(id = blog_id)
	except BlogPost.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	#user = request.user
	#print(user)
	#print(blog_post.author)


	if request.method == 'GET':
		serializer = BlogPostSerializer(blog_post)
		return Response(serializer.data)


@api_view(['PUT',])
def api_update_blog_view(request, blog_id):

	try:
		blog_post = BlogPost.objects.get(id = blog_id)
	except BlogPost.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	#print(user)
	#print(blog_post.author)

	if blog_post.author != user:
		return Response({"message" : "You can't update this post because you have not created this post"})

	if request.method == 'PUT':
		serializer = BlogPostSerializer(blog_post, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data[SUCCESS] = UPDATE_SUCCESS
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
# @permission_classes([])
# @authentication_classes([])
def api_delete_blog_view(request, blog_id):

	try:
		blog_post = BlogPost.objects.get(id = blog_id)
	except :
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	user = request.user
	#print(user)
	#print(blog_post.author)

	if blog_post.author != user:
		return Response({"message" : "You can't delete this post because you have not created this post"})


	if request.method == 'DELETE':
		operation = blog_post.delete()
		data = {}
		if operation:
			data[SUCCESS] = DELETE_SUCCESS
		return Response(data=data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_create_blog_view(request):

	account = request.user

	blog_post = BlogPost(author=account)

	if request.method == 'POST':
		serializer = BlogPostSerializer(blog_post, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
