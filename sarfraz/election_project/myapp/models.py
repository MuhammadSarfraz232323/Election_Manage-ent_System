from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=20)
    cnic=models.CharField(max_length=30,primary_key=True)
    def __str__(self):
        return self.username
@receiver(post_save,sender=User)
def user_craete_action(sender,instance,created,*args,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("User data has been created !! ")
    else:
        print("The user creation has been failed !! ")    

class Home(models.Model):
    name=models.CharField(max_length=20)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=100)
    id_no=models.CharField(max_length=15,primary_key=True)
    phone_number=models.CharField(max_length=20)
    email_adress=models.EmailField(max_length=40,null=False)
    password=models.CharField(max_length=40)
   

class Election_introduction(models.Model):
    party_flag=models.ImageField(upload_to='voter_panel')   
    party_name=models.CharField(max_length=100)
    party_symbol=models.ImageField(upload_to="candidate_image")
    candidate_name=models.CharField(max_length=30) 
    image=models.ImageField(upload_to='party_symbol')

class Party1(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    Adress=models.CharField(max_length=100)
    Id_no=models.CharField(max_length=100)

class Vote_casting(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=40)
    phone_number=models.CharField(max_length=40,default="")
    password=models.CharField(max_length=40)
    party=models.CharField(max_length=40)
    id_no=models.CharField(max_length=15,primary_key=True)

class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="videos")   
    def __str__(self):
        return self.caption
     



