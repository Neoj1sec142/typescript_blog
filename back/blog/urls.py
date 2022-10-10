from .serializers import *
from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    # path('posts/<str:username>', PostDetail.as_view(), name='user_post_detail'),
]