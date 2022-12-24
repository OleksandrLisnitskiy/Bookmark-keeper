from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def settings(request):
    return render(request, "home/settings.html")


def tasks(request):
    return render(request, "home/task_group.html")