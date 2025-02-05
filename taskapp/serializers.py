from rest_framework import serializers
from .models import Task

#Serializers are using here to convert the complex datatypes into JSON format

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']   #Fields visible in the API response
        read_only_fields = ['id', 'created_at', 'updated_at','deleted_at']   #User can only read this fields
