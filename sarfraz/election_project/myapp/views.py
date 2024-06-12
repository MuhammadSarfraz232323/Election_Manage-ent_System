from django.shortcuts import render,redirect,reverse
from myapp.form import Super_user,Main_user,Simple,Request,Account_verification,Login,Voterf,Login_user,Casting,Mannual_result,Check_registration,My_video
from django.http import HttpResponse,HttpResponseRedirect
from election_project import settings
from django.contrib.auth.models import User
from myapp.models import Home,Election_introduction,Video,Vote_casting,Party1,Video
from  django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth import authenticate,login,logout
import random
from myapp.serializers import Homeserializer,Partyserializer,Main_serializer,Vote_serializer,Introduction_serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,serializers,generics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from myapp.models import UserProfile
from django.db import transaction

# we are now creating different apis to test the functionalit of ours models 


# ----------------------------------------------------  for home table 
@api_view(['post','DELETE','GET'])
def introduction(request):
    sarfraz=Election_introduction.objects.all()
    if request.method=="POST":
        my_serializer=Introduction_serializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serailizer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_bad_request)
    elif request.method=="DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK) 
    elif request.method=="GET":
        my_serializer=Introduction_serializer(sarfraz,many=True)
        return Response(my_serializer.data,status=status.HTTP_200_OK)

        
def my_decorator(a):
    def new(request,*args,**kwargs):
        if request.user.is_authenticated:
            return a(request,*args,**kwargs)
            print("The user is authenticated ")
        else:
            my_url=reverse('front-page')
            return HttpResponseRedirect(my_url)
    # print('You are at the main function !! ')
    return new
def my_admin(a):
    def new(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return a(request) 
        else:
            messages.success(request,"Only staff members are allowed to get the admin entry !! ")
            my_url=reverse('home')
            return HttpResponseRedirect(my_url)
    return new        
@api_view(['GET','POST','DELETE'])  
def Home_api(request):
    sarfraz=Home.objects.all()
    if request.method=="POST":
        my_dataz=Home.objects.all()
        my_serializer=Homeserializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    

    elif request.method == "GET":
        my_serializer=Homeserializer(sarfraz,many=True)
        return Response(my_serializer.data) 
    elif request.method=='DELETE':
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)     
@api_view(['DELETE'])         
def user_profile(request):
    sarfraz=UserProfile.objects.all()
    if request.method=="DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET','PATCH','DELETE'])
def home_id(request,id):
    sarfraz=Home.objects.get(pk=id)
    if request.method=="GET":
        my_serializer=Homeserializer(sarfraz)
        return Response(my_serializer.data,status=status.HTTP_200_OK)   

    elif request.method=="PATCH":
        sarfraz.name=request.data.get('name',sarfraz.name)
        sarfraz.father_name=request.data.get('father_name',sarfraz.father_name) 
        sarfraz.id_no=request.data.get('id_no',sarfraz.id_no)
        sarfraz.phone_number=request.data.get('phone_number',sarfraz.phone_number),       
        sarfraz.email_adress=request.data.get('email_adress',sarfraz.email_adress)
        sarfraz.password=request.data.get('password',sarfraz.password)
        sarfraz.save()
        my_serializer=Homeserializer(sarfraz)
        return Response(my_serializer.data,status=status.HTTP_200_OK)
    elif request.method=="DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)   

# -------------------------------------------------------      for party table        


@api_view(['PUT','PATCH','GET'])  
def party(request,id):
    try:
        sarfraz=Party1.objects.get(pk=id)  
    except Party1.DoesNotExist:   
        return Response(status=status.HTTP_404_NOT_FOUND)       
    if request.method=="PUT":
        my_serializer=Partyserializer(sarfraz,data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
    elif request.method=="PATCH":
        sarfraz.name=request.data.get('name',sarfraz.name)
        sarfraz.father_name=request.data.get('father_name',sarfraz.father_name)
        sarfraz.phone_number=request.data.get('phone_number',sarfraz.phone_number)
        sarfraz.Adress=request.data.get('Adress',sarfraz.Adress)
        sarfraz.Id_no=request.data.get('Id_no',sarfraz.Id_no)
        sarfraz.save()
        my_serializer=Partyserializer(sarfraz)
        return Response(my_serializer.data,status=status.HTTP_201_CREATED)
    elif request.method=="GET":
        my_serializer=Partyserializer(sarfraz)
        return Response(my_serializer.data,status=status.HTTP_200_OK)  

@api_view(['GET','POST'])    
def party_1(request):        
    sarfraz=Party1.objects.all()
    if request.method=="GET":
        my_serializer=Partyserializer(sarfraz,many=True)
        return Response(my_serializer.data,status=status.HTTP_200_OK)

    elif request.method=="POST":
        my_serializer=Partyserializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data,status=status.HTTP_201_CREATED) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

#for vote casting 
@api_view(['POST','GET','DELETE'])
def vote(request):
    sarfraz=Vote_casting.objects.all()
    if request.method=="POST":
        my_serializer=Vote_serializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        my_serializer=Vote_serializer(sarfraz,many=True)
        return Response(my_serializer.data,status=status.HTTP_201_CREATED) 
    elif request.method=="DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)    

@api_view(['POST','GET','DELETE'])
def create_user(request):
    sarfraz=User.objects.all()
    if request.method=="POST":
        my_serializer=Main_serializer(data=request.data)
        my_serializer.save()
        return Response(status=status.HTTP_201_CREATED) 
    elif request.method=="GET":
        my_serializer=Main_serializer(sarfraz)
        return Response(myserializer.data,status=status.HTTP_200_OK) 
    elif request.method=="DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)       

# Original views functions are here 

import sqlite3
connection=sqlite3.connect('db.sqlite3',check_same_thread=False)
cursor=connection.cursor()

def empty(a,nn=0):
    for i in a:
        nn+=1
    del a[0:nn]
    return a    


name_list=[]
first_name_list=[]
last_name_list=[]
id_no_list=[]
phone_number_list=[]
email_list=[]
adress_list=[]
password_list=[]
otp_list=[]
check_variable=["sarfraz"]

@login_required(login_url='front-page')
def homepage(request): 
    return render(request,"index.html")
@transaction.atomic
def account_verification(request):
    form=Account_verification()
    if request.method=="POST":
        form=Account_verification(request.POST)
        if form.is_valid():
            otp=request.POST['otp_variable']
            print(otp)
            if int(otp_list[0])==int(otp):
                check_variable.insert(0,1)
                hash_password=make_password(password_list[0])
                print("home created ")    
                sarfraz=User.objects.create(
                    username=name_list[0],
                    first_name=first_name_list[0],
                    last_name=last_name_list[0],
                    email=email_list[0],
                    password=hash_password
                )
                sarfraz.save()
                sarfraz1=UserProfile.objects.create(
                    phone_number=phone_number_list[0],
                    cnic=id_no_list[0],
                    name=name_list[0]
                    )
                sarfraz1.save()
                print('profile created ')    
                messages.success(request,"The Account created successfully ! You can now login !!!")
                my_url=reverse('home')
                return HttpResponseRedirect(my_url)
            else:
                return HttpResponse("<h1 align='center'>Sorry,<br>The OTP provided by you is incorrect.Please  try again </h1>")    
    context={
        "form":form
    }
    return render(request,"verification.html",context)

def main_portal(request):
    obj=Election_introduction.objects.all()
    context={
        "object":obj
    }
    return render(request,"mainpage.html",context)
def resend_otp(request):
    if check_variable[0]==1:
        return HttpResponse("<h1 align='center'>Your Account has been verified now you can log in </h1>")
    else:
        empty(otp_list)
        otp=random.randint(100000,999999)
        otp_list.append(otp)
        subject="OTP reverification "
        message=f"Dear {name_list[0]},  \n  Your Reverified OTP is  \n   {otp}  \n PLease Do not share  it with any one "
        from_email=settings.EMAIL_HOST_USER
        to_list=[
        email_list[0]
        ]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        return HttpResponse(f"<h1 align='center'>A reverified OTP has been sended to {email_list[0]} please check the email and verify your account </h1>")
   
def simple_login(request):
    form=Login()
    if request.method=="POST":
        form=Login(request.POST)
        if form.is_valid():
            name=request.POST['username']
            password1=request.POST['password']
            cnic=request.POST['id_no']
            user=authenticate(username=name,password=password1)
            if user is not None:
                login(request,user)
                my_url=reverse('home')
                return HttpResponseRedirect(my_url)
            else:
                messages.success(request,"There is some problem !! Please try again !! ")    
    context={
        "form":form
    }
    return render(request,"login.html",context) 

@my_decorator    
def logout_main(request):
    logout(request)
    my_url=reverse('front-page')
    return HttpResponseRedirect(my_url)   

@my_admin
def voter(request):
    form=Voterf()
    if request.method=="POST":
        form=Voterf(request.POST,request.FILES)
        if form.is_valid():
            Election_introduction.objects.create(**form.cleaned_data)
            name=request.POST['party_name']
            try:
                query=f"""create table {name}(
                name varchar(100),
                father_name varchar(100),
                phone_number varchar(100),
                party varchar(100),
                password varchar(100),
                id_no varchar(100))"""
                cursor.execute(query)
                connection.commit()
                messages.success(request,"A new electiuon has been organized to the election panel ")
            except:
                messages.success(request,"There is some problem !!Please try again !!")
        else:
            print(form.errors)
    context={
        "form":form
    }            
    return render(request,"voter.html",context)

def vote_casting(request,id):
    sarfraz=Election_introduction.objects.get(pk=id)
    form=Casting()
    if request.method=="POST":
        form=Casting(request.POST)
        if form.is_valid():
            name1=request.POST['name']
            father_name1=request.POST['father_name']
            phone_number1=request.POST['phone_number']
            password1=request.POST['password']
            id_no1=request.POST['id_no']
            # party1=request.POST['party']
            if User.objects.filter(username=name1).exists():
                print("sarfraz")
                if Vote_casting.objects.filter(id_no=id_no1).exists():
                    messages.success(request,"This user have already casted his vote !! ")
                else:    
                    try:
                        query=f"insert into {sarfraz.party_name} values ('{name1}','{father_name1}','{phone_number1}','{sarfraz.party_name}','{password1}','{id_no1}')"
                        cursor.execute(query)
                        connection.commit()
                        print(sarfraz.party_name)
                        Vote_casting.objects.create(
                        name=name1,
                        father_name=father_name1,
                        phone_number=phone_number1,
                        password=password1,
                        party=sarfraz.party_name,
                        id_no=id_no1
                        )
                        Vote_casting.objects.create(**form.cleaned_data)
                        messages.success(request,f"Dear {name} ! You have casted you vote successfully !! ")
                        my_url=reverse('home')
                        return HttpResponseRedirect(my_url)
                    except:
                        messages.success(request,"You have alreaday casted your vote !! ")
    context={
        "form":form
    }        
    return render(request,"vote_casting.html",context)
def watch_video(request):
    obj=Video.objects.all()
    context={
        "object":obj
    }
    return render(request,"video.html",context)

def contact_page(request):
    return render(request,'contact.html')    

@my_decorator
def complete(request):
    obj=Vote_casting.objects.all()
    context={
        "object":obj
    }
    return render(request,"complete_result.html",context)       

def ecp_overview(request):
    return render(request,"overview.html")


def registration(request):
    return render(request,'registration.html')    

def verify_registration(request):
    form=Check_registration()
    if request.method=="POST":
        form=Check_registration(request.POST)
        if form.is_valid():
            name=request.POST['name']
            id_no=request.POST['id_no']
            query="select* from  myapp_vote_casting "
            cursor.execute(query)
            variable=cursor.fetchall()
            id_check_list=[]
            for i in variable:
                id_check_list.append(i[4])
            if id_no in id_check_list:
                return HttpResponse("<h1 align='center'>The person with this data has already casted the vote </h1>")    
            else:
                pass   
            registration_list=[]
            query="select* from myapp_home"
            cursor.execute(query)
            variable=cursor.fetchall()
            for i in variable:
                registration_list.append(i[0])
                registration_list.append(i[2])
            if name in registration_list and id_no in registration_list:
                return HttpResponse("<h1 align='center'>Your registration has already done.Please login to cast your vote </h1>")
            else:
                return HttpResponse("<h1 align='center'>No user with this data is registered </h1>")
    context={
        "form":form
    }            
    return render(request,"verify_registration.html",context)    

@my_decorator
def check_registration(request):
    obj=Home.objects.all()
    context={
        "object":obj
    }
    return render(request,"check_registrations.html",context) 

def detail(request):
    form=Request()
    if request.method=="POST":
        form=Request(request.POST)
        if form.is_valid():
            name=request.POST['username']
            try:
                sarfraz=User.objects.get(username=name)
                print(sarfraz.username)
                print(sarfraz.password)
                context={
                "name":sarfraz.username,
                "first_name":sarfraz.first_name,
                "last_name":sarfraz.last_name,
                'password':sarfraz.password
                }
                my_subject="Data Recovery Email "    
                html_message=render_to_string("user_data_email.html",context)
                plain_message=strip_tags(html_message)
                message=EmailMultiAlternatives(
                  body=plain_message,
                    subject=my_subject,
                    from_email=None,
                        to=[
                            sarfraz.email
                        ]
                )
                message.attach_alternative(html_message,'text/html')
                try:
                    message.send()
                    print("Email is sent successfully !! ")
                except:
                    messages.success(request,"There is some problem ! Please try again !!! ")    
            except:
                messages.success(request,"No user with this data is present !! ")        
        else:
            print(form.errors)
    context={
        "form":form
    }            
    return render(request,'main_user.html',context)

def detail(request,id):
    form=Request()
    if request.method=="POST":
        form=Request(request.POST)
        if form.is_valid():
            name=request.POST['username']
            try:
                sarfraz=User.objects.get(pk=id)
                print(sarfraz.username)
                print(sarfraz.password)
                context={
                "name":sarfraz.username,
                "first_name":sarfraz.first_name,
                "last_name":sarfraz.last_name,
                'password':sarfraz.password
                }
                my_subject="Data Recovery Email "    
                html_message=render_to_string("user_data_email.html",context)
                plain_message=strip_tags(html_message)
                message=EmailMultiAlternatives(
                  body=plain_message,
                    subject=my_subject,
                    from_email=None,
                        to=[
                            sarfraz.email
                        ]
                )
                message.attach_alternative(html_message,'text/html')
                try:
                    message.send()
                    print("Email is sent successfully !! ")
                except:
                    messages.success(request,"There is some problem ! Please try again !!! ")    
            except:
                messages.success(request,"No user with this data is present !! ")        
        else:
            print(form.errors)
    context={
        "form":form
    }            
    return render(request,'main_user.html',context)    
@my_decorator
def video_function(request):
    form=My_video()
    if request.method=="POST":
        form=My_video(request.POST,request.FILES)
        if form.is_valid():
            Video.objects.create(**form.cleaned_data)
            messages.success(request,"Video uploaded successfully !! ")
        else:
            messages.success(irequest,"There is some problem !Please try again !! ")
    context={
        "form":form
    }        
    return render(request,'video_upload.html',context)
def general_election(request):
    return render(request,'general_election.html')    

def Voter_instructions(request):
    return render(request,"for_voter.html")

def front_page(request):
    form=Main_user()
    if request.method=="POST":
        form=Main_user(request.POST)
        if form.is_valid():
            empty(name_list)  #We are using the empty function in order to delete all the data from the existing list so that new user comes with new data   
            empty(email_list)
            empty(otp_list)
            empty(first_name_list)
            empty(last_name_list)
            empty(phone_number_list)
            empty(password_list)
            empty(id_no_list)
            # print(form.cleaned_data)
            name=request.POST['username']
            name_list.append(name)
            first_name=request.POST['first_name']
            first_name_list.append(first_name)
            last_name=request.POST['last_name']
            last_name_list.append(last_name)
            phone_number=request.POST['phone_number']
            phone_number_list.append(phone_number)
            email=request.POST['email']
            email_list.append(email)
            id_no=request.POST['cnic']
            id_no_list.append(id_no)
            password=request.POST['password']
            password_list.append(password)
            check_list=[]
            def check_the_existance(name):
                return User.objects.filter(username=name).exists()
            if check_the_existance(name):
                messages.success(request,"The username is already registered !! ")
            else:
                otp=random.randint(100000,999999) 
                otp_list.append(otp)
                print(otp_list)
                my_subject="Account verification on ECP"
                html_message=render_to_string('email.html',{"otp":otp})
                plain_message=strip_tags(html_message)
                message=EmailMultiAlternatives(
                body=plain_message,
                subject=my_subject,
                from_email=None,
                to=[
                    email
                    ]
                    )
                message.attach_alternative(html_message,"text/html")
                variable=False
                try:
                    print(otp)
                    # message.send()
                    variable=True
                except:
                    return HttpResponse("<h1 align='center'>There is some problem please try again</h1>")
                    variable=False    
                if variable:
                    messages.success(request,"Account created successfully please Put the OTP you received to Verify your vote ")
                    return redirect('Account_verification/')
                else: 
                    return HttpResponse("</h align='center'>There is some problem !! Please try again </h1>")    
        print(form.errors)
    context={
        "form":form
    } 
    return render(request,"front_page.html",context)
@transaction.atomic
def main_user_create(request):
    form=Super_user()    
    if request.method=="POST":
        form=Super_user(request.POST)
        if form.is_valid():
            username=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            UserProfile.objects.create(
                phone_number=phone_number,
                cnic=cnic,
                name=username
            )
    context={
        "form":form
    }        
    return render(request,'main_user_create.html',context)