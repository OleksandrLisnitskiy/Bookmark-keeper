from django.shortcuts import render
from .models import Groups, Tasks
# Create your views here.


def index(request):
    groups = Groups.objects.all()
    all_tasks = Tasks.objects.all()
    return render(request, "home/index.html", {"groups": groups, "tasks": all_tasks})


def settings(request):
    return render(request, "home/settings.html")


def tasks(request, group_id):
    tasks_from_group = Tasks.objects.filter(group_id__exact=group_id)
    return render(request, "home/task_group.html", {"tasks": tasks_from_group})