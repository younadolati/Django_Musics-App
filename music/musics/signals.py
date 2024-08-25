from django.db.models.signals import post_save
from django.dispatch import receiver
from musics.models import Test
from django.utils.text import slugify

@receiver(post_save,sender=Test)
def signal(sender,instance,*args,**kwargs):
    if not instance.slug:
        slug=slugify(str(instance.name)+"-"+str(instance.id)) 
        # if Test.objects.filter(slug=slug).exists():
            # slug="%s-%s"%(slug,instance.id)
            # slug=slugify(instance.name) 


        instance.slug=slug
        print(instance.slug)
        instance.save()
    