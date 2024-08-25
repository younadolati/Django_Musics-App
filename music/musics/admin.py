from django.contrib import admin
from .models import Musics,Comment,Test

class CommentInline(admin.StackedInline):
    model=Comment
    extra=0

class PersonAdmin(admin.ModelAdmin):
    inlines=[CommentInline]

class Test1(admin.ModelAdmin):
    list_display=['name']
    # prepopulated_fields={"slug":["name"]}

# Register your models here.

admin.site.register(Musics,PersonAdmin)
admin.site.register(Test,Test1)
admin.site.register(Comment)
