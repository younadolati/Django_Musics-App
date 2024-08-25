from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Musics (models.Model):
    title=models.CharField(max_length=30)
    singer=models.CharField(max_length=30)
    likes=models.ManyToManyField(User,related_name="likes")
    slug=models.SlugField(max_length=30,unique=True,blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self) :
        return self.title
    
    
    def get_absolute_url(self):
        return f'/details/{self.id}'
    
class Test(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True) 

    slug_field_name = 'slug'
    slug_from = 'name'
 
    def __unicode__(self):
        return self.name+"-"+str(self.pk)
    
   
   

    

    
class Comment(models.Model):
    music=models.ForeignKey(Musics,on_delete=models.CASCADE,related_name="music")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    comment=models.TextField()

    def __str__(self) :
        return self.music.title
 
 


