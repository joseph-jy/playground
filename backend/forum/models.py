from django.db import models

class Forum(models.Model):
  title = models.CharField(max_length=20)
  forum_category_id = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  class Meta:
    indexes = [
      models.Index(fields = ["forum_category_id"])
    ]

class ForumCategory(models.Model):
  name = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)

class Topic(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  user_id = models.PositiveIntegerField()
  forum_id = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
  content = models.TextField()
  user_id = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
  user_id = models.PositiveIntegerField()
  target_id = models.PositiveIntegerField()
  target_type = models.CharField(max_length=10, choices=[('topic', 'Topic'), ('comment', 'Comment')])
