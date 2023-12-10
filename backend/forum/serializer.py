from rest_framework import serializers
from .models import ForumCategory, Forum, Topic, Comment

class ForumCategorySerialzier(serializers.ModelSerializer):
  class Meta:
    model = ForumCategory
    fields = "__all__"

class ForumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Forum
    fields = "__all__"

class TopicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topic
    fields = "__all__"

class CommentSerialzier(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"