from django.contrib import admin

from .models import Manufacturer, HeatingModel, ErrorCode

admin.site.register(Manufacturer)
admin.site.register(HeatingModel)


class ErrorCodeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ErrorCode._meta.get_fields()]


admin.site.register(ErrorCode, ErrorCodeAdmin)
