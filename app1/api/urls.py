from django.conf.urls import url, include
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'app1'

urlpatterns = [
    url(r'^login/', views.Login222.as_view(), name='login222'),
    url(r'^create_profile/', views.ProfileListCreateAPIView.as_view(), name='create_profile'),
    url(r'^create_profile2/', views.ProfileCreateAPIView.as_view(), name='create_profile2'),
    url(r'^editdel_profile/(?P<id>[0-9]+)$', views.ProfileUpdateDeleteAPIView.as_view(), name='editdel_profile'),
    url(r'^create_cooperation/', views.HamkariListCreateAPIView.as_view(), name='create_cooperation'),
    url(r'^editdel_cooperation/(?P<id>[0-9]+)$', views.HamkariUpdateDeleteAPIView.as_view(), name='editdel_cooperation'),
    url(r'^create_user/', views.UserListCreateAPIView.as_view(), name='create_user'),
    url(r'^create_user2/', views.UserCreateAPIView.as_view(), name='create_user2'),
    url(r'^editdel_user/(?P<id>[0-9]+)$', views.UserUpdateDeleteAPIView.as_view(), name='editdel_user'),
    url(r'^edit_user/(?P<id>[0-9]+)$', views.UserEditAPIView.as_view(), name='edit_user'),
    url(r'^create_farakhan/', views.FarakhanListCreateAPIView.as_view(), name='create_farakhan'),
    url(r'^editdel_farakhan/(?P<id>[0-9]+)$', views.FarakhanUpdateDeleteAPIView.as_view(), name='editdel_farakhan'),
    url(r'^create_profile_ready/', views.Profile_readyListCreateAPIView.as_view(), name='create_profile_ready'),
    url(r'^editdel_profile_ready/(?P<id>[0-9]+)$', views.Profile_readyUpdateDeleteAPIView.as_view(), name='editdel_profile_ready'),
    url(r'^create_profile_present/', views.Profile_presentListCreateAPIView.as_view(), name='create_profile_present'),
    url(r'^editdel_profile_present/(?P<id>[0-9]+)$', views.Profile_presentUpdateDeleteAPIView.as_view(), name='editdel_profile_present'),
    url(r'^create_cooperation_code/', views.Hamkari_codeListCreateAPIView.as_view(), name='create_cooperation_code'),
    url(r'^editdel_cooperation_code/(?P<id>[0-9]+)$', views.Hamkari_codeUpdateDeleteAPIView.as_view(), name='editdel_cooperation_code'),
]
