from django.urls import path
from blog.api.views import(
	api_detail_blog_view,
	api_update_blog_view,
	api_delete_blog_view,
	api_create_blog_view,
)

app_name = 'blog'

urlpatterns = [
	path('<int:blog_id>/', api_detail_blog_view),
	path('<int:blog_id>/update', api_update_blog_view),
	path('<int:blog_id>/delete', api_delete_blog_view,),
	path('create', api_create_blog_view),
]