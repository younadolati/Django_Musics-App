from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from musics.sitemaps import StaticViewSitemap,MusicSitemap
from django.views.generic.base import TemplateView
from django.urls import path,include

sitemaps={'static':StaticViewSitemap,'musics':MusicSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("musics.urls")),
    path('sitemap.xml/', sitemap,{'sitemaps':sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt",content_type="text/plain")),



]
