from django.contrib import admin

from .models import Manufacturer,HeatingModel,ErrorCode

admin.site.register(Manufacturer)
admin.site.register(HeatingModel)
admin.site.register(ErrorCode)