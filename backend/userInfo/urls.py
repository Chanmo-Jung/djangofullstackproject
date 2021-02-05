#backend/post/urls.py
from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
import sys
urlpatterns = [
#     # path('', views.ListPost),
    # http://39.118.174.168:8000/api/
    path('login/', obtain_jwt_token),
    path('verify/', verify_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('current_user/', views.current_user),
    path('register/', views.UserList.as_view()),
    # path('api/login/', views.LoginAPI.as_view()),
    # path('api/user/', views.UserAPI.as_view()),
#     path('api/list/', views.ListAPI.as_view({'get':'list'})),
#     path('api/<int:pk>/', views.UpdateAPI.as_view()),
#     path('api/<int:pk>/delete/', views.DeleteAPI.as_view()),
]
