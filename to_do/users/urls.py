from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

app_name="users"

urlpatterns = [
    url(r'list/', views.UserList.as_view(), name='user-list'),
    url(r'create/', views.UserCreate.as_view(), name='user-create'),
    url(r'detail/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
