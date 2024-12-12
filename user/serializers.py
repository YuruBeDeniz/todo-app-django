from django.contrib.auth.models import User
from rest_framework import serializers
from todoapp.models import Task

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    # tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'tasks']