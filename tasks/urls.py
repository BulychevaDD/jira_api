from django.urls import path

from tasks.views import ProjectView, TaskView, CommentView

urlpatterns = [
    path('project', ProjectView.as_view(), name='project'),
    path('task', TaskView.as_view(), name='task'),
    path('comment', CommentView.as_view(), name='comment'),
]
