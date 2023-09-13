from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage,name='homepage'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('thanks/', views.thanks, name='thanks'),
    path('add/',views.add,name='add'),
    path('',views.index,name='index')
]