from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class StandardLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class StandardCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'created'