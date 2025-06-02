from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse, FileResponse
from .models import Project, CV, ProjectFile
import io
import zipfile

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Project
    ordering = ["-date"]
    context_object_name = "projects"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


def download_project_files_zip(request, slug):
    project = get_object_or_404(Project, slug=slug)
    files = project.files.all()
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for f in files:
            zip_file.writestr(f.file.name.split("/")[-1], f.file.read())
    zip_buffer.seek(0)
    response = HttpResponse(zip_buffer, content_type="application/zip")
    response['Content-Disposition'] = f'attachment; filename={project.slug}_files.zip'
    return response

class SingleProjectView(View):
    def is_stored_project(self, request, project_id):
        stored_projects = request.session.get("stored_projects")
        if stored_projects is not None:
            is_saved_for_later = project_id in stored_projects
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        project = get_object_or_404(Project, slug=slug)
        context = {
            "project": project,
            "project_tags": project.tags.all(),
            "saved_for_later": self.is_stored_project(request, project.id)
        }
        return render(request, "blog/project-detail.html", context)

    def post(self, request, slug):
        project = get_object_or_404(Project, slug=slug)
        stored_projects = request.session.get("stored_projects", [])
        if "remove" in request.POST:
            if project.id in stored_projects:
                stored_projects.remove(project.id)
                request.session["stored_projects"] = stored_projects
        else:
            if project.id not in stored_projects:
                stored_projects.append(project.id)
                request.session["stored_projects"] = stored_projects
        return redirect("project-detail-page", slug=slug)

class StoredProjectsView(View):
    def get(self, request):
        stored_projects = request.session.get("stored_projects")
        context = {}
        if stored_projects is None or len(stored_projects) == 0:
            context["projects"] = []
            context["has_projects"] = False
        else:
            projects = Project.objects.filter(id__in=stored_projects)
            context["projects"] = projects
            context["has_projects"] = projects.exists()
        return render(request, "blog/stored-projects.html", context)

    def post(self, request):
        remove_id = request.POST.get("remove_project_id")
        stored_projects = request.session.get("stored_projects", [])
        if remove_id:
            try:
                stored_projects.remove(int(remove_id))
                request.session["stored_projects"] = stored_projects
            except ValueError:
                pass
        return redirect("stored-projects")


def cv_view(request):
    cv = CV.objects.last()
    filename = cv.file.name.split("/")[-1] if cv and cv.file else ""
    return render(request, "blog/cv.html", {"cv": cv, "filename": filename})

class AllProjectsView(ListView):
    template_name = "blog/all-projects.html"
    model = Project
    context_object_name = "all_projects"
    ordering = ["-date"]

def download_project_file(request, file_id):
    file_obj = get_object_or_404(ProjectFile, id=file_id)
    response = FileResponse(file_obj.file.open("rb"), as_attachment=True, filename=file_obj.file.name.split("/")[-1])
    return response
