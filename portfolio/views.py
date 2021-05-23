from django.shortcuts import render, get_object_or_404

from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/welcome.html', {'projects': projects})


def work(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/work.html', {'projects': projects})


def work_detail(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'portfolio/detail.html', {'project': project})


def about(request):
    return render(request, 'portfolio/about.html')
