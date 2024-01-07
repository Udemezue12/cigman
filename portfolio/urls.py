# urls.py
from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('profiles', views.ProfileViewSet, basename='profiles')
router.register('skills', views.SkillViewSet, basename='skills')
router.register('projects', views.ProjectViewSet)
router.register('experiences', views.ExperienceViewSet)
router.register('educations', views.EducationViewSet)
router.register('certifications', views.CertificationViewSet)
router.register('projects', views.ProjectViewSet)
router.register('authors', views.AuthorViewSet)
router.register('awards', views.AwardViewSet)



profiles_router =routers.NestedDefaultRouter(router, 'profiles', lookup='profile')
# profiles_router.register('skils', views.SkillViewSet, basename='profile-skills')

profiles_router.register(
    'images', views.ProfileImageViewSet, basename='profile-images')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(profiles_router.urls)),
    
]
