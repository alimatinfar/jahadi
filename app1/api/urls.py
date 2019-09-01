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
    url(r'^create_farakhan/', views.FarakhanListCreateAPIView.as_view(), name='create_farakhan'),
    url(r'^editdel_farakhan/', views.FarakhanUpdateDeleteAPIView.as_view(), name='editdel_farakhan'),
    url(r'^create_profile_ready/', views.Profile_readyListCreateAPIView.as_view(), name='create_profile_ready'),
    url(r'^editdel_profile_ready/', views.Profile_readyUpdateDeleteAPIView.as_view(), name='editdel_profile_ready'),
    url(r'^create_profile_present/', views.Profile_presentListCreateAPIView.as_view(), name='create_profile_present'),
    url(r'^editdel_profile_present/', views.Profile_presentUpdateDeleteAPIView.as_view(), name='editdel_profile_present'),
]
