
from django.urls import path
from . import views

urlpatterns = [
    path('',views.allblogs,name='allblogs'),
    path('<int:blog_id>/',views.details,name='detail') #look for int after blog_id
]
