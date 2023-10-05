# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.sparql_query, name='sparql_query'),
    path('api/result/', views.sparql_result_as_json, name='sparql_result_as_json'),
]
