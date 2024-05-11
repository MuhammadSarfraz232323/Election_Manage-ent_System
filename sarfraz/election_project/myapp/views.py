from django.shortcuts import render,redirect
from myapp.form import main_user,Simple,Request,Account_verification,Login,Voterf,Login_user,Casting,Mannual_result,Check_registration,My_video
from django.http import HttpResponse
from election_project import settings
from django.contrib.auth.models import User
from myapp.models import Home,Election_introduction,Video,Vote_casting,Party1,Video
from  django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth import authenticate,login
import random
from myapp.serializers import Homeserializer,Partyserializer,Main_serializer,Vote_serializer,Introduction_serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,serializers,generics

# we are now creating different apis to test the functionalit of ours models 


# ----------------------------------------------------  for home table 
@api_view(['post','DELETE'])
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
@api_view(['POST','GET'])
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

@api_view(['POST','GET'])
def create_user(request):
    sarfraz=User.objects.all()
    if request.method=="POST":
        my_serializer=Main_serializer(data=request.data)
        my_serializer.save()
        return Response(status=status.HTTP_201_CREATED) 
    elif request.method=="GET":
        my_serializer=Main_serializer(sarfraz)
        return Response(myserializer.data,status=status.HTTP_200_OK)    

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
email_list=[]
otp_list=[]
check_variable=["sarfraz"]
def homepage(request):
    form=Simple()
    if request.method=="POST":
        form=Simple(request.POST)
        if form.is_valid():
            empty(name_list)  #We are using the empty function in order to delete all the data from the existing list so that new user comes with new data   
            empty(email_list)
            empty(otp_list)
            # print(form.cleaned_data)
            name=request.POST['name']
            email=request.POST['email_adress']
            id_no=request.POST['id_no']
            check_list=[]
            query="select* from myapp_home"
            cursor.execute(query)
            variable=cursor.fetchall()
            for i in variable:
                check_list.append(i[5])
            if id_no in check_list:
                return HttpResponse("<h1 align='center'>The user with this ID is already registered here !! Please try to login </h1>")    
            else:    
                otp=random.randint(100000,999999) 
                otp_list.append(otp)
                name_list.append(name)
                email_list.append(email)
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
                    message.send()
                    variable=True
                except:
                    return HttpResponse("<h1 align='center'>There is some problem please try again</h1>")
                    variable=False    
                if variable:
                    Home.objects.create(**form.cleaned_data)
                    messages.success(request,"Account created successfully please Put the OTP you received to Verify your vote ")
                    return redirect('Account_verification/')
                else: 
                    return HttpResponse("</h align='center'>There is some problem !! Please try again </h1>")    
        print(form.errors)
    context={
        "form":form
    }        
    
    return render(request,"index.html",context)
def account_verification(request):
    form=Account_verification()
    if request.method=="POST":
        form=Account_verification(request.POST)
        if form.is_valid():
            otp=request.POST['otp_variable']
            if int(otp_list[0])==int(otp):
                check_variable.insert(0,1)
                return redirect('main_portal/')
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
            name=request.POST['name']
            password=request.POST['password']
            cnic=request.POST['id_no']
            query="select* from myapp_home"
            cursor.execute(query)
            variable=cursor.fetchall()
            connection.commit()
            check_list=[]
            for i in variable:
                check_list.append(i[0])
                check_list.append(i[4])
                check_list.append(i[5])
            print(check_list)    
            if name in check_list and password in check_list and cnic in check_list:
                query="select* from myapp_vote_casting "
                cursor.execute(query)
                variable=cursor.fetchall()
                second_check=[]
                for i in variable:
                    second_check.append(i[5])
                print(second_check)    
                if cnic in second_check:
                    return HttpResponse("<h1 align='center'>The user with this cnic have already casted his vote. Thanks for visiting us !!</h1>")
                else:    
                    return redirect('main_portal/')
            else:
                return HttpResponse("<h1 align='center'>There is some problem in your data provided.Please try again </h1>")    
    context={
        "form":form
    }
    return render(request,"login.html",context) 

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
                return HttpResponse("<h1 align='center'>A new party has been organized to election panel successfully </h1>")
            except:
                return HttpResponse("<h1 align='center'>There is some problem please try again </h1>")
        else:
            print(form.errors)
    context={
        "form":form
    }            
    return render(request,"voter.html",context)

def create_user(request):
    form=Login_user()
    if request.method=="POST":
        form=Login_user(request.POST)
        if form.is_valid():
            name=request.POST['name']
            password=request.POST['password']
            user=authenticate(username=name,password=password)
            if user is not None:
                print(user)
                login(request,user)
                return redirect('Admin/')
            else:
                return HttpResponse("<h1 align='center'>There is some problem Please try again</h1>")    
    context={
        "form":form
    }
    return render(request,"admin_login.html",context)  
def vote_casting(request):
    form=Casting()
    if request.method=="POST":
        form=Casting(request.POST)
        if form.is_valid():
            name1=request.POST['name']
            father_name1=request.POST['father_name']
            phone_number1=request.POST['phone_number']
            password1=request.POST['password']
            id_no1=request.POST['id_no']
            party1=request.POST['party']
            query="select * from myapp_home"
            cursor.execute(query)
            variable=cursor.fetchall()
            connection.commit()
            my_list=[]
            for i in variable:
                my_list.append(i[4])
            if password1 not in my_list:  
                return HttpResponse("<h1 align='center'>You password does not match </h1>")      
            else:
                pass
            try:
                query=f"insert into {party1} values ('{name1}','{father_name1}','{phone_number1}','{party1}','{password1}','{id_no1}')"
                cursor.execute(query)
                connection.commit()
                Vote_casting.objects.create(**form.cleaned_data)
                return HttpResponse(f"<h1 align='center'>Dear {name1},<br>You have casted your vote for {party1} </h1>")
            except:
                return HttpResponse("<h1 align='center'>Sorry !!There is some problem please try again </h1>")
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
            cnic=request.POST['id_no']
            query=f"select* from myapp_home where id_no = '{cnic}' "
            cursor.execute(query)
            variable=cursor.fetchone()
            print(variable[0])
            print(variable[5])
            if cnic==variable[5]:
                my_subject="Data recovery Email "
                context={
                    "name":variable[0],
                    "father_name":variable[1],
                    "phone_number":variable[2],
                    "email":variable[3],
                    "password":variable[4], 
                    'id_no':variable[5]                   
                }
                html_message=render_to_string("user_data_email.html",context)
                plain_message=strip_tags(html_message)
                message=EmailMultiAlternatives(
                    body=plain_message,
                    subject=my_subject,
                    from_email=None,
                    to=[
                        variable[3]
                        ]
                )
                message.attach_alternative(html_message,'text/html')
                try:
                    message.send()
                except:
                    return HttpResponse("<h1 align='center'>There is some problem !! Please try again </h1>")    
                return HttpResponse("<h1 align='center'>Email sent successfully.Chaeck your registration data to cast your vote </h1>")
            else:
                return HttpResponse("<h1 align='center'>Sorry,<br>This cnic is not registered Please try with registered CNIC </h1>")
    context={
        "form":form
    }        
    return render(request,'request_for_email.html',context)    

def double_verification(request):
    return HttpResponse("<h1 align='center'>You are already on the required page </h1>")


def main_user_create(request):
    form=main_user()
    if request.method=="POST":
        form=main_user(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            return HttpResponse("<h1 align='center'>A new user created successfully  !!!!!!!</h1>")
        else:
            print(form.errors)
    context={
        "form":form
    }            
    return render(request,'main_user.html',context)


def video_function(request):
    form=My_video()
    if request.method=="POST":
        form=My_video(request.POST,request.FILES)
        if form.is_valid():
            Video.objects.create(**form.cleaned_data)
            return HttpResponse("<h1 align='center'>Your video is uploaded successfully </h1>")
        else:
            return HttpResponse("<h1 align='center'>Failed to upload your video</h>")    
    context={
        "form":form
    }        
    return render(request,'video_upload.html',context)
def general_election(request):
    return render(request,'general_election.html')    




