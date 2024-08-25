from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='app'

urlpatterns=[
    path('',views.members,name='home'),
    path('<int:id>/',views.details,name='details'),
    path('<slug:slug>/',views.test,name='test'),
    path('signup/',views.signupuser,name='signup'),
    path('autosearch/',views.search,name='autosearch'),
    # path('members/details/likes/<int:id>',views.likes,name='likes'),





]
urlpatterns+=staticfiles_urlpatterns()