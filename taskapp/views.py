from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from .pagination import TaskPagination

#TaskViewSet is used to handle the CRUD operations related to the Task model

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(deleted_at__isnull=True) #return task that have not been soft deleted
    serializer_class = TaskSerializer 
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] #Allows users to filter, search, and order API results.
    filterset_fields = ['status', 'created_at'] #enables filtering by status and created date
    search_fields = ['title', 'description']    #enables searching by title and desription
    ordering_fields = ['created_at']            #enables ordering
    ordering = ['-created_at']                  #enables ordering by latest updated data

    def perform_destroy(self, instance):
        instance.soft_delete()                #soft deleting task when an instance called the soft_delete()
