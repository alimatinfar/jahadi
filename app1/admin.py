from django.contrib import admin
from .models import Profile,  Hamkari, Farakhan, Profile_present, Profile_ready, Hamkari_code, Post
# Register your models here.
admin.site.register(Profile)
admin.site.register(Hamkari)
admin.site.register(Hamkari_code)
admin.site.register(Farakhan)
admin.site.register(Profile_present)
admin.site.register(Profile_ready)
admin.site.register(Post)
