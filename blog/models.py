from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
class ProjectFile(models.Model):
    file = models.FileField(upload_to="project_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    files = models.ManyToManyField(ProjectFile, blank=True)
    image = models.ImageField(upload_to="projects", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="projects")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class CV(models.Model):
    file = models.FileField(upload_to="cv/")
    uploaded_at = models.DateTimeField(auto_now_add=True)