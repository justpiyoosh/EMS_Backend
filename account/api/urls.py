from django.urls import path
from account.api.views import(
	registration_view,
	account_properties_view,
	update_account_view,
	account_info,
	fetch_all_usernames
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('login', obtain_auth_token, name="login"), # -> see accounts/api/views.py for response and url info
	path('<str:username>',account_info),     #to view the information of a user with the username 
	path('properties',account_properties_view),
	path('properties/update',update_account_view),
	path('users/fetch_all_usernames/<str:username>', fetch_all_usernames )
]