
from django.conf.urls import url, include
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'app1'

urlpatterns = [
    url(r'^login/', views.Login222.as_view(), name='login'),
    url(r'^create_profile/', views.ProfileListCreateAPIView.as_view(), name='create_profile'),
    url(r'^editdel_profile/', views.ProfileUpdateDeleteAPIView.as_view(), name='editdel_profile'),
    url(r'^create_cooperation/', views.HamkariListCreateAPIView.as_view(), name='create_cooperation'),
    url(r'^editdel_cooperation/', views.HamkariUpdateDeleteAPIView.as_view(), name='editdel_cooperation'),
    url(r'^create_user/', views.UserListCreateAPIView.as_view(), name='create_user'),
    url(r'^editdel_user/', views.UserUpdateDeleteAPIView.as_view(), name='editdel_user'),
]