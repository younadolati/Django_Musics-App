from django.urls import path
from . import views

urlpatterns=[
    path("",views.show_musics,name="musics"),
    path("page/<int:page>/",views.show_musics,name="musics"),
    path("tests/",views.show_tests,name="tests"),
    path("details/<int:id>/",views.details,name="details"),
    path('<slug:slug>/',views.test,name='test'),
    path("details/likes/<int:id>",views.like_show,name="likes"),






]