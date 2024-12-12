from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        owner = serializers.ReadOnlyField(source='owner.username')
        # read_only_fields = ['owner']