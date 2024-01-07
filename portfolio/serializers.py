from rest_framework import serializers

from . import models




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['id', 'user', 'bio']  # Add other fields as needed

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'

class CertifcationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certification
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publication
        fields = '__all__'

class SimpleProfileSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['first_name', "last_name"]
class SimpleAuthorSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['first_name', "last_name"]
class AwardSerializer(serializers.ModelSerializer):
    profile = SimpleProfileSerilaizer()
    author = SimpleAuthorSerilaizer()
    class Meta:
        model = models.Award
        fields = ['id', 'organization', 'author', 'profile', 'description']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileImage
        fields = ['id', 'image']

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return ProfileImage.objects.create(profile_id=profile_id, **validated_data)


