from rest_framework import serializers

from tasks.models import Task
from django.contrib.auth.admin import UserAdmin
from .models import User



class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='User.username')

    class Meta:
        model = Task
        fields = ('url', 'id', 'name', 'description', 'duration', 'user', 'PRIORITY_CHOICES', 'priority', 'dead_line','time_remaining', 'done','time_done', 'created', 'modified')
        extra_kwargs = {
            'url': {
                'view_name': 'tasks:task-detail',
            }
        }
