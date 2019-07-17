from django.urls import path
from . import views

urlpatterns = [
	# http://localhost:8000/blog/1
	path('<int:blog_pk>')
]
