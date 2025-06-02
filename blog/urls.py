from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("projects", views.AllProjectsView.as_view(), name="projects-page"),
    path("projects/<slug:slug>", views.SingleProjectView.as_view(), name="project-detail-page"),
    path("stored-projects", views.StoredProjectsView.as_view(), name="stored-projects"),
    path("cv", views.cv_view, name="cv"),
    path("projects/file/<int:file_id>/download", views.download_project_file, name="download-project-file"),
    path("projects/<slug:slug>/download-all", views.download_project_files_zip, name="download-project-files-zip")
]