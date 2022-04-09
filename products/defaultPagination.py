from rest_framework.pagination import PageNumberPagination

from ._customPaginator import CustomPaginator

class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    django_paginator_class = CustomPaginator