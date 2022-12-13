from django.urls import path
from myApp import views

app_name='myApp'

urlpatterns = [
		path('add/', views.add),
		path('list/', views.list),
		
		]