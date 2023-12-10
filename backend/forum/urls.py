from django.urls import path
from .views import ForumCategoryListView

urlpatterns = [
    path('forum-categories/', ForumCategoryListView.as_view(), name ='forum-categoryies-list-view')
]
