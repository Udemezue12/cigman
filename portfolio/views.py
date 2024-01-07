# views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter
from portfolio.paignation import DefaultPaignation
from portfolio.permissions import IsAdminOrReadOnly, ViewAuthorHistoryPermission, ViewAwardrHistoryPermission, ViewProfileHistoryPermission, ViewCertificateHistoryPermission
from portfolio.serializers import CertifcationSerializer, EducationSerializer, ExperienceSerializer, ProfileSerializer, PublicationSerializer, SkillSerializer, ProjectSerializer, AwardSerializer, ProfileImageSerializer, AuthorSerializer
from .models import Profile, Skill, Project, Award, Author, Publication, Certification, Education, Experience, ProfileImage
from .paignation import DefaultPaignation


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.prefetch_related('images').all()
    serializer_class = ProfileSerializer

    @action(detail=True, permission_classes=[ViewProfileHistoryPermission])
    def history(self, request, pk):
        return Response('ok')

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        profile = Profile.objects.get(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPaignation

    # def get_queryset(self):
    #     return Profile.objects.filter(profile_id=self.kwargs['profile_pk'])

    # def get_serializer_context(self):
    #     return {'profile_id':self.kwargs['profile_pk']}


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['gender', 'email']
    pagination_class = DefaultPaignation
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

    @action(detail=True, permission_classes=[ViewAuthorHistoryPermission])
    def history(self, request, pk):
        return Response('ok')

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Author.objects.get(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = AuthorSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AuthorSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertifcationSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAdminOrReadOnly()]

    @action(detail=True, permission_classes=[ViewCertificateHistoryPermission])
    def history(self, request, pk):
        return Response('ok')


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    pagination_class = DefaultPaignation

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAdminOrReadOnly()]

    @action(detail=True, permission_classes=[ViewAwardrHistoryPermission])
    def history(self, request, pk):
        return Response('ok')


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileImageViewSet(viewsets.ModelViewSet):
    # queryset = ProductImage.objects.get()
    serializer_class = ProfileImageSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

    def get_serializer_context(self):
        return {'profile_id': self.kwargs['profile_pk']}

    def get_queryset(self):
        return ProfileImage.objects.filter(product_id=self.kwargs['profile_pk'])
