from django.contrib import admin
from .models import Tag, Author, Project, CV, ProjectFile


class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ['file', 'uploaded_at']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectFile, ProjectFileAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(CV)