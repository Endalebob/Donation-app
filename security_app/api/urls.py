from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from security_app.api.views import *

urlpatterns = [
    path('login/',obtain_auth_token, name= 'login' ),
    path('register/',registration, name= 'register' ),
    path('logout/',logout_view, name= 'logout' ),
    path('user-list/',get_all_user, name= 'user-list' ),
    path('user-detail/<str:username>',editprofile, name= 'user-detail' ),

]