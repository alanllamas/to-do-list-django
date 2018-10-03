from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ('url', 'id', 'name', 'description', 'duration', 'user', 'PRIORITY_CHOICES', 'priority', 'dead_line', 'done', 'created', 'modified')
        extra_kwargs = {
            'url': {
                'view_name': 'tasks:task-detail',
            }
        }
