from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from tasks.models import Project, Task, Comment
from tasks.serialzers import ProjectSerializer


class CommentView(views.APIView):
    def post(self, request, format=None):
        username = request.user.username

        if not {'task', 'content'}.issubset(set(request.data.keys())):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.create(
            task_id=request.data['task'],
            content=request.data['content'],
            user=User.objects.get(username__iexact=username),
        )
        comment.save()

        return Response(status=status.HTTP_200_OK)


class TaskView(views.APIView):
    def post(self, request, format=None):
        if not {'project', 'name', 'description'}.issubset(set(request.data.keys())):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        task = Task.objects.create(
            project_id=request.data['project'],
            name=request.data['name'],
            description=request.data['description']
        )
        task.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        if 'id' not in request.data.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Task.objects.get(id=request.data['id']).delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, format=None):
        if 'id' not in request.data['data'].keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        task = Task.objects.get(id=request.data['data']['id'])
        task.is_done = not task.is_done
        task.save()

        return Response(status=status.HTTP_200_OK)


class ProjectView(views.APIView):
    def get(self, request, format=None):
        username = request.user.username

        projects = Project.objects.filter(users__username__iexact=username)
        projects_serializer = ProjectSerializer(projects, many=True)
        projects_data = projects_serializer.data

        return Response(projects_data)

    def post(self, request, format=None):
        username = request.user.username

        if 'name' not in request.data.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if Project.objects.filter(name__iexact=request.data['name']).count() > 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        project = Project.objects.create(name=request.data['name'])
        project.users.add(User.objects.get(username__iexact=username))
        project.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        if 'id' not in request.data.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Project.objects.get(id=request.data['id']).delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, format=None):
        if not {'user', 'project'}.issubset(set(request.data['data'].keys())):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(id=request.data['data']['user'])
        project = Project.objects.get(id=request.data['data']['project'])
        project.users.add(user)
        project.save()

        return Response(status=status.HTTP_200_OK)
