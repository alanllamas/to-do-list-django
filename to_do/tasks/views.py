from tasks.models import Task
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from tasks.serializers import TaskSerializer
 
 
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
 
    def get_queryset(self):
        return Task.objects.all().filter(user=self.request.user)