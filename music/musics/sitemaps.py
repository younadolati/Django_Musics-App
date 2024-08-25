from django.contrib.sitemaps import Sitemap
# from django.db.models.base import Model
from .models import Musics
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    protocol='http'
    
    def items(self) :
        return ['musics']
    
    def location(self,item):
        return reverse(item)


class MusicSitemap(Sitemap):
    protocol='http'
    changefreq='always'
    priority='1.0'

    def items(self):
        return Musics.objects.all()
    
        

    