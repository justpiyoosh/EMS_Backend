from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.permissions import IsAuthenticated

from account.api.serializers import RegistrationSerializer , AccountPropertiesSerializer
from rest_framework.authtoken.models import Token
from account.models import Account
from django.http import JsonResponse

# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):

	if request.method == 'POST':
		print( request.data )
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			data['dp_code'] = account.dp_code
			token = Token.objects.get(user=account).key
			data['token'] = token
			data['status'] = 201
			data['status_message'] = "Nice"
		else:
			data = serializer.errors
			data['status'] =  400
			data['status_message'] = "Not Nice"
		return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_properties_view(request):
	try:
		account = request.user
	except:
		return Response({"message" : "Account Does not exist"})

	if request.method == 'GET':
		serializer = AccountPropertiesSerializer(account)
		return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_account_view(request):
	try:
		account = request.user
	except:
		return Response({"message" : "Account Does not exist"})

	if request.method == 'PUT':
		serializer = AccountPropertiesSerializer(account , data =request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data["response"] = "Acoount updated successfully"
			return Response(data=data)
		return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([])
def account_info(request , username):
	query_user = Account.objects.get(username = "justpiyoosh")
	data = { "email" : query_user.email ,
	         "username" : query_user.username,
			 "date_joined" : query_user.date_joined         }
	return Response(data)

@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def fetch_all_usernames(request, username):
	#users  = cursor.execute('''select username from Account where username like '%ju%' ''')
	try:
		data = []
		users = Account.objects.filter(username__contains=username)
		for user in users:
			data.append(user.username)
		usernames = {}
		usernames["names"] = data 
		if len(data) == 0:
			return Response({"message" : "Sorry we don't have users with this username"})
		return JsonResponse(usernames)
	except:
		return Response({"message" : "Sorry we don't have users with this username"})
	