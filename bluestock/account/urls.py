from django.urls import path
from .views import registerUser, user_login,user_logout,user_home

urlpatterns = [
    path('', user_home, name = 'home'),
    path('login/', user_login, name = 'login'),
    path('register/', registerUser, name = 'register'),
    path('logout', user_logout, name = 'home'),
   
]
