from django.contrib import admin
from .models import Profile,  Hamkari, Farakhan, Profile_present, Profile_ready, Hamkari_code, Post
from django_jalali.admin.filters import JDateFieldListFilter

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )
    list_display = ('title', 'content', 'date')
    list_editable = ('title',)
    list_display_links = ('content',)
    search_fields = ('title', 'content')



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user' ,'first_name', 'last_name')
    search_fields = ('user__username' ,'first_name', 'last_name')


class HamkariAdmin(admin.ModelAdmin):
    list_display = ('profile',)
    search_fields = ('profile__user__username',)


class Hamkari_codeAdmin(admin.ModelAdmin):
    list_display = ('national_code',)
    search_fields = ('national_code',)


class FarakhanAdmin(admin.ModelAdmin):
    list_display = ('farakhan_title',)
    search_fields = ('farakhan_title',)


class Profile_presentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'farakhan')
    search_fields = ('profile__user__username', 'farakhan')


class Profile_readyAdmin(admin.ModelAdmin):
    list_display = ('profile', 'farakhan')
    search_fields = ('profile__user__username', 'farakhan')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Hamkari, HamkariAdmin)
admin.site.register(Hamkari_code, Hamkari_codeAdmin)
admin.site.register(Farakhan, FarakhanAdmin)
admin.site.register(Profile_present, Profile_presentAdmin)
admin.site.register(Profile_ready, Profile_readyAdmin)
# admin.site.register(Post, PostAdmin)
