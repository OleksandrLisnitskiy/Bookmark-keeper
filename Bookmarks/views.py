from django.shortcuts import render, redirect
from .models import Groups, Tasks
from .forms import AddGroup, AddTask, EditTask, EditGroup
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
    context = {"tasks": tasks_from_group, 'groups': groups, 'group_name': group_name, 'group_id':group_id}

    if request.method == 'POST':

        if "delete-item" in request.POST:
            task_id = int(request.POST["delete-item"])
            Tasks.objects.filter(pk=task_id).delete()
        if "delete-group" in request.POST:
            Groups.objects.filter(pk=group_id).delete()
            return redirect('index')

    context["edit_form"] = EditTask()
    context["add_form"] = AddTask()
    context["edit_group"] = EditGroup(initial={'group_name': str(group_name)})

    return render(request, "home/task_group.html", context)


def edit_task(request, group_id, task_id):
    edit_form = EditTask(request.POST)
    if edit_form.is_valid():
        if edit_form.cleaned_data["edit_deadline"] == '':
            deadline = Tasks.objects.filter(pk=task_id).values()['edit_deadline']
        else:
            deadline = edit_form.cleaned_data["edit_deadline"]
        Tasks.objects.filter(pk=task_id).update(task=edit_form.cleaned_data["task"], deadline=deadline)
    return redirect('tasks', group_id)


def add_task(request, group_id):
    add_form = AddTask(request.POST)
    if add_form.is_valid():
        new_task = Tasks(group=Groups.objects.get(pk=group_id), task=add_form.cleaned_data["task_name"],
                         deadline=add_form.cleaned_data["deadline"])
        Groups.objects.filter(pk=group_id).update(number_of_tasks=Groups.objects.get(pk=group_id).number_of_tasks + 1)
        new_task.save()
    return redirect("tasks", group_id)


def edit_group(request, group_id):
    edit_group_form = EditGroup(request.POST)

    if edit_group_form.is_valid():

        Groups.objects.filter(pk=group_id).update(group_name=edit_group_form.cleaned_data["group_name"])
    return redirect('tasks', group_id)
