from django.contrib.auth.models import User
from rest_framework import serializers

from tasks.models import Project, Comment, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', )


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'is_done', 'comments', )


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'users', 'tasks', )
