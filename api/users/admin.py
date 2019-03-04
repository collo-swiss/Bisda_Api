from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from api.users.models import User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass
