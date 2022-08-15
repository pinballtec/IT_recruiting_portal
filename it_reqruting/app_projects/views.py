from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Tag
from django.contrib import messages
from .forms import ProjectForm, ReviewForm


# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'app_projects/projects.html', context)


def project(request, pk):
    project_single = Project.objects.get(id=pk)
    tags = project_single.tags.all()
    return render(request, 'app_projects/single-project.html', {'project': project_single})


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'app_projects/project_form.html', {'form': form})


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'app_projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'app_projects/delete.html', context)


def filter_projects_by_tags(request, tag_slug):
    """filter function for objects(db)"""
    tag = get_object_or_404(Tag, slug=tag_slug)
    projects = Project.objects.filter(tags__in=[tag])
    context = {'projects': projects}
    return render(request, "projects/projects.html", context)


def project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    tags = project.tags.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.getVoteCount
        messages.success(request, 'Your vote has been sent')
        return redirect('project', project_slug=project.slug)
    return render(request, 'projects/single-project.html', {'project': project, 'form': form})
