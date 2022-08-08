from django.shortcuts import render
from .models import Project
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'app_projects/projects.html', context)


def project(request, pk):
    project_single = Project.objects.get(id=pk)
    tags = project_single.tags.all()
    return render(request, 'app_projects/single-project.html', {'project': project_single})