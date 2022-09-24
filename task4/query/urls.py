from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('api',views.api,name='upload'),
    path('query',views.query,name='upload'),
    path('top',views.top,name='upload')
]