from django.conf.urls import url
from . import views


app_name = 'appfront'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cooperation/$', views.cooperation, name='cooperation'),
    url(r'^cooperation_code/$', views.cooperation_code, name='cooperation_code'),
    url(r'^create_farakhan/$', views.create_farakhan, name='create_farakhan'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_profile/(?P<id>[0-9]+)$', views.edit_profile, name='edit_profile'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^folder_gallery/$', views.folder_gallery, name='folder_gallery'),
    url(r'^farakhan_detail/(?P<id>[0-9]+)$', views.farakhan_detail, name='farakhan_detail'),
    url(r'^farakhan_detail_sherkat/(?P<id>[0-9]+)$', views.farakhan_detail_sherkat, name='farakhan_detail_sherkat'),
    url(r'^success/$', views.success, name='success'),

]