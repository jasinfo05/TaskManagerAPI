from rest_framework.pagination import PageNumberPagination

#Defines how many pages have to be shown per API reponse. Maximum limit is set to 50

class TaskPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50