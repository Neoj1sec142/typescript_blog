from rest_framework import serializers
from .models import Post
from users.models import User
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    # users = UserSerializer(
    #     many=False, 
    #     read_only=True, 
    #     source='user'
    # )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
    )
    
    class Meta:
        model = Post
        fields = '__all__'
        extra_fields = ('users')
        ordering = ('-date_created')
