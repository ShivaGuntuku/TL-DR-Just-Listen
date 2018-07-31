from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Posts
		fields = ("title", "content")

class TokenSerializer(serializers.Serializer):
	"""
	This serializer serilizes the token data
	"""

	token = serializers.CharField(max_length=255)
	