from django import forms

class Simple(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your father name "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number "
    }))
    email_adress=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))
    id_no=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your id no ",
        "pattern":"[0-9]{5}-[0-9]{7}-[0-9]{1}"
    }))

class Account_verification(forms.Form):
    otp_variable=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your OTP"
    }))  

class Login(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))      
    email_adress=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your Email adress "
    }))
    id_no=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your CNIC",
        "pattern":"[0-9]{5}-[0-9]{7}-[0-9]{1}"
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))
class Voterf(forms.Form):
    candidate_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the name of Candidate "
    }))
    party_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the name of party "
    }))    
    party_flag=forms.ImageField(label='Upload the party Flag Image ',widget=forms.ClearableFileInput(attrs={
        "class":"form-control "
    }))
    image=forms.ImageField(label='Upload image of candidate',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))
    party_symbol=forms.ImageField(label='Upload the Image of Party Symbol ',widget=forms.ClearableFileInput(attrs={
        "class":"form-control "
    }))

class Login_user(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))    
    email_adress=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress"
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))
class Casting(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your father name "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number"
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))  
    id_no=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your ID no ",
        "pattern":"[0-9]{5}-[0-9]{7}-[0-9]{1}"
    }))
class Mannual_result(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the name of party "
    }))    

class Check_registration(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))    
    id_no=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter  your CNIC  ",
        "pattern":"[0-9]{5}-[0-9]{7}-[0-9]{1}"
    }))

class Request(forms.Form):
    id_no=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your CNIC number "
    }))    
class Main_user(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your username  "
    }))    
    first_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your first name "
    }))
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your last name "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number "
    }))
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your Email Adress"    
    }))
    cnic=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your CNIC "
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))
class My_video(forms.Form):
    video=forms.FileField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))