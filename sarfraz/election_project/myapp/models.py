from django.db import models

# Create your models here.

class Home(models.Model):
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=50)
    id_no=models.CharField(max_length=15,primary_key=True)
    phone_number=models.CharField(max_length=20)
    email_adress=models.EmailField(max_length=20,null=False)
    password=models.CharField(max_length=40)
   

class Election_introduction(models.Model):
    party_flag=models.ImageField(upload_to='voter_panel')   
    party_name=models.CharField(max_length=100)
    party_symbol=models.ImageField(upload_to="party_symbols")
    candidate_name=models.CharField(max_length=30) 

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
     



