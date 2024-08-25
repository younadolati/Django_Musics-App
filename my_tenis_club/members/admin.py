from django.contrib import admin
from .models import Members,Person,Useraccount,Test



class PersonAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','phone','joined_date']
    list_filter=['joined_date']
    search_fields=['firstname','lastname']
    ordering=['joined_date']

class Test1(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={"slug":["name"]}




admin.site.register(Members,PersonAdmin)
admin.site.register(Test,Test1)
admin.site.register(Useraccount)
admin.site.register(Person)
# Register your models here.
