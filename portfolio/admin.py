from django.contrib import admin
from django.utils.html import format_html, urlencode

from portfolio import models

# Register your models here.


class ProfileImageInline(admin.TabularInline):
    model = models.ProfileImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bio']
    list_per_page = 10
    list_select_related = ['user', 'author']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    ordering = ['user__first_name', 'user__last_name']
    inlines = [ProfileImageInline]


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_select_related = ['profile']
    autocomplete_fields = ['profile']
    list_per_page = 10
    list_editable = ['description']
    search_fields = ['name']


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date']
    list_per_page = 10
    list_select_related = ['profile']
    autocomplete_fields = ['profile']
    list_editable = ['company', 'start_date', 'end_date']


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution',
                    'start_date', 'end_date', 'description']
    list_per_page = 10
    list_select_related = ['profile']
    autocomplete_fields = ['profile']
    list_editable = ['institution', 'start_date', 'end_date', 'description']


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date']
    list_per_page = 10
    list_select_related = ['profile', 'author']
    autocomplete_fields = ['profile', 'skills', 'author']
    list_editable = ['description', 'start_date', 'end_date']
    search_fields = ['title']


@admin.register(models.Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization',
                    'date_issued']
    list_per_page = 10
    list_select_related = ['profile']
    autocomplete_fields = ['profile']
    list_editable = ['issuing_organization', 'date_issued']
    list_display_links = ['name']


@admin.register(models.Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'year_awarded']
    list_per_page = 10
    list_editable = ['organization', 'year_awarded']
    list_display_links = ['title']
    autocomplete_fields = ['profile', 'author']
    list_select_related = ['profile', "author"]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',  'membership',
                    'email', 'github_username', 'twitter_username']
    list_editable = ['membership']
    search_fields = ['last_name']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.register(models.Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author']
    list_per_page = 10

    list_editable = ['description']
    list_display_links = ['title']
    autocomplete_fields = ['profile', 'author']
    list_select_related = ['profile', "author"]
