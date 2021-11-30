from django.contrib import admin
from .models import UbntModelTest, Startprocess, Listipubnt


class BbAdmin(admin.ModelAdmin):
    list_display = ('ipubntone', 'nameubnt', 'nameubntline')


admin.site.register(UbntModelTest, BbAdmin)
#admin.site.register(Startprocess)
#admin.site.register(Listipubnt)
