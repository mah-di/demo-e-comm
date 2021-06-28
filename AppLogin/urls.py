from django.contrib.auth import login
from django.urls import path
from .views import signup, user_login, user_logout, user_profile


app_name = 'AppLogin'


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
]