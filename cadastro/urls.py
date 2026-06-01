from django.urls import path
from .views import login_view, logout_view, cadastro_publico, cadastro_admin

app_name = 'cadastro'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', cadastro_publico, name='publico'),
    path('admin/', cadastro_admin, name='admin'),
]
