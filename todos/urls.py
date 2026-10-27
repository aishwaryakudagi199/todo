from django.urls import path 
from . import views
urlpatterns = [
    path('addtasks/',views.addtasks,name='addtasks'),
]