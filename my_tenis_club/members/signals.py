# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Musics
# from django.utils.text import slugify

# @receiver(pre_save,sender=Musics)
# def signals(sender,inctance,*args,**kwargs):
#     if not inctance.slug:
#         slug=slugify(inctance.title) 

#         slug="%s-%s"%(slug,inctance.id)
#     inctance.slug=slug
#     inctance.save()