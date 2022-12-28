from django.shortcuts import render
from .models import Groups, Tasks
from .forms import AddGroup
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
    tasks_from_group = Tasks.objects.filter(group_id__exact=group_id)
    context = {"tasks": tasks_from_group, 'groups': groups}
    return render(request, "home/task_group.html", context)