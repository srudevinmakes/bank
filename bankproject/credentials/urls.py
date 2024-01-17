from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    # Add other URL patterns as needed
]
