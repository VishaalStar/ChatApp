from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.chat, name='chat'),
    path('<str:room_name>/', views.room, name='room'),
]