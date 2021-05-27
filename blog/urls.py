from django.urls import path
from . import views
# from .views import PostCreateView
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.blog, name='blog'),
    # path('post/new/', PostCreateView.as_view(), name='post-detail'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]