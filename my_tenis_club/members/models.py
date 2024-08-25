from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from ckeditor.fields import RichTextField
from django.urls import reverse

class Members(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    phone=models.IntegerField()
    joined_date=models.DateField()

    class Meta:
        ordering=('-joined_date',)

    def __str__(self):
        return self.firstname
    
    def get_absolute_url(self):
        return reverse("app:details",kwargs={'id':self.id})


def get_profile_image(self,filename):
    return 'profile/profile_images/'+str(self.pk)+'/profile_image.png'

class Person(models.Model):
    name=models.CharField(max_length=30)
    singer=models.CharField(max_length=40)
    # likes=models.ManyToManyField(Useraccount)
 
 


    
    def __str__(self):
        return self.name

class Test(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(unique=True,null=False,default="") 

    def __str__(self) -> str:
        return super().__str__()
    

def get_default_image():
    return 'profile/profile_defaultimage/defaultimage'

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        if not username:
            raise ValueError("Users must have an username address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class Useraccount(AbstractBaseUser):
    email = models.EmailField( verbose_name="email address", max_length=255, unique=True,)
    username=models.CharField(max_length=30,unique=True,)
    profile_image=models.ImageField(upload_to=get_profile_image,default=get_default_image,blank=False,null=False,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
     
    
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
