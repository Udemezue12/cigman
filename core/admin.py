from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.models import User
from tags.models import TaggedItem
from portfolio.models import Profile
from portfolio.admin import ProfileAdmin, ProfileImageInline


# @admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProfileAdmin(ProfileAdmin):
    inlines = [TagInline, ProfileImageInline]


admin.site.unregister(Profile)
admin.site.register(Profile, CustomProfileAdmin)
