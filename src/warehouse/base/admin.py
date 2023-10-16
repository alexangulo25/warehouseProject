from django.contrib import admin
from .models import warehouse
from import_export.admin import ImportExportModelAdmin
# from .models import File


# Register your models here.

admin.site.register(warehouse)
# admin.site.register(File)

class uploadAdmin(ImportExportModelAdmin):
    list_display = ('item', 'quantity', 'WarehouseId')

