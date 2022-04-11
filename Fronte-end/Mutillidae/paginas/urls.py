from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hints/', views.hints, name='hints'),
    path('log/', views.log, name='log'),
    path('data/', views.data, name='data'),
    path('Owasp/<id>/', views.verOwasp, name='owasp'),
]