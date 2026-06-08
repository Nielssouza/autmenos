from django.urls import path
from .views import login_view, logout_view, cadastro_publico, cadastro_admin

app_name = 'cadastro'

urlpatterns = [
    path('', cadastro_publico, name='publico'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/', cadastro_admin, name='admin'),
]
