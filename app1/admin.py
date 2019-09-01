from django.contrib import admin
from .models import Profile,  Hamkari, Farakhan, Profile_present, Profile_ready
# Register your models here.
admin.site.register(Profile)
admin.site.register(Hamkari)
admin.site.register(Farakhan)
admin.site.register(Profile_present)
admin.site.register(Profile_ready)
