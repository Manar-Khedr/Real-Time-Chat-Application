from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


#URL pages --> import in urls.py of the application
urlpatterns = [
    path('',views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]