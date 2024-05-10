from rest_framework import serializers
from django.contrib.auth.models import User

from myapp.models import Home,Party1,Vote_casting,Election_introduction

class Homeserializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields=['name','father_name','id_no','phone_number','email_adress','password']

class Partyserializer(serializers.ModelSerializer):
    class Meta:
        model=Party1
        fields=[
            'name','father_name','phone_number','Adress','Id_no'
        ]        
class Main_serializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=[
            'username','email','first_name','last_name','password'
        ]      

class Vote_serializer(serializers.ModelSerializer):
    class Meta:
        model=Vote_casting
        fields=[
            'name','father_name','phone_number','password','party','id_no'
        ]         
class Introduction_serializer(serializers.ModelSerializer):
    class Meta:
        model=Election_introduction
        fields=[
            'party_flag','party_name','party_symbol','candidate_name','image'
        ]
