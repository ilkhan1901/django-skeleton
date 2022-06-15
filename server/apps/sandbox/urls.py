from django.urls import path, include

from .views import *

app_name = 'sandbox'

urlpatterns = [
	path('',index)
]