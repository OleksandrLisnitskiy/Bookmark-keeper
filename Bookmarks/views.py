from django.shortcuts import render, redirect
from .models import Groups, Tasks
from .forms import AddGroup, AddTask
# Create your views here.


def index(request):
    groups = Groups.objects.all()
    all_tasks = Tasks.objects.all()
    context = {"groups": groups, "tasks": all_tasks}
    if request.method == 'POST':
        form = AddGroup(request.POST)

        if form.is_valid():

            new_group = Groups(group_name=form.cleaned_data["group_name"])
            new_group.save()
            context["form"] = AddGroup()

            return render(request, "home/index.html", context)
    else:
        form = AddGroup()
    context["form"] = form
    return render(request, "home/index.html", context)


def settings(request):
    groups = Groups.objects.all()
    context = {'groups': groups}
    return render(request, "home/settings.html", context)


def tasks(request, group_id):

    groups = Groups.objects.all()
    group_name = Groups.objects.get(pk=group_id).group_name
    tasks_from_group = Tasks.objects.filter(group_id__exact=group_id)
    context = {"tasks": tasks_from_group, 'groups': groups, 'group_name': group_name}

    if request.method == 'POST':

        if "delete-item" in request.POST:
            task_id = int(request.POST["delete-item"])
            Tasks.objects.filter(pk=task_id).delete()
        form = AddTask(request.POST)
        if form.is_valid():

            new_task = Tasks(group=Groups.objects.get(pk=group_id), task=form.cleaned_data["task"], deadline=form.cleaned_data["deadline"])
            Groups.objects.filter(pk=group_id).update(number_of_tasks=Groups.objects.get(pk=group_id).number_of_tasks+1)
            new_task.save()
            context["form"] = AddTask()

            return redirect("tasks", group_id)

    else:
        form = AddTask()
    context["form"] = form

    return render(request, "home/task_group.html", context)

