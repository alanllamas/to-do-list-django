from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views

app_name = 'tasks'
urlpatterns = [
    url(r'list', views.TaskList.as_view(), name='task-list'),
    url(r'detail/(?P<pk>[0-9]+)/', views.TaskDetail.as_view(), name='task-detail'),
]
