from rest_framework.pagination import PageNumberPagination


class DefaultPaignation(PageNumberPagination):
    page_size = 12