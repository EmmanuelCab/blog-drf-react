from rest_framework import serializers
from .models import Post
from apps.category.serializers import CategorySerializers

class PostSerializer(serializers.ModelSerializer):
    thumbnail=serializers.CharField(source='get_thumbnail')
    video=serializers.CharField(source='get_video')
    category=CategorySerializers()
    class Meta:
        model = Post
        fields=[
            'blog_uuid',
            'title',
            'slug',
            'thumbnail',
            'video',
            'description',
            'excerpt',
            'category',
            'published',
            'status',
        ]