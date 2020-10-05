from django.shortcuts import render
from projects.models import Project

# Django ORM query to select all objects in the Project table
def home(request):
    projects = Project.objects.all() # query database for all objects in Project table
    return render(request, 'projects/home.html', {'projects':projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) # This query retrieves the project with primary key, pk, equal to that in the function argument
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)
