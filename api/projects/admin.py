from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from api.projects.models import Project, Industry


# Register your models here.
admin.site.register(Project)
admin.site.register(Industry)

