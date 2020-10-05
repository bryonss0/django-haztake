from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # hook up the root URL of our app to the project_index view
    path("<int:pk>/", views.project_detail, name="project_detail"), # URL to be /1, or /2, and so on, depending on the pk of the project
]
