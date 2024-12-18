from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]