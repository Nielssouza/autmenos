from django.urls import path
from . import views

app_name = 'ajuda'

urlpatterns = [
    path('', views.central_ajuda, name='central'),
]