from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<slug:project_slug>/', views.project, name="project"),
    path('create-project', views.create_project, name='create-project'),
    path('update-project<str:pk>', views.update_project, name='update-project'),
    path('delete<str:pk>', views.deleteProject, name='delete'),
    path('tag/<slug:tag_slug>', views.filter_projects_by_tags, name="tag_filter"),
]