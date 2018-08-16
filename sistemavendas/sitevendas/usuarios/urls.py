from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'
urlpatterns = [
    path('registrar/', views.RegisterView.as_view(), name='registrar'),
    path('login/',  auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
