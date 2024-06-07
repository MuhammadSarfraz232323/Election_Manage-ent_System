from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import Home,Election_introduction,Party1,Vote_casting,Video
from django.contrib.auth.admin import UserAdmin as AuthAdminUser
from myapp.models import UserProfile
class UserProfileInline(admin.StackedInline):
    model=UserProfile
    can_delete=False

class AccountsAdminUser(AuthAdminUser):
    def add_view(self,*args,**kwargs):
        self.inlines=[]
        return super(AccountsAdminUser,self).add_view(*args,**kwargs)
    def change_view(self,*args,**kwargs):
        self.inlines=[UserProfileInline]
        return super(AccountsAdminUser,self).chage_view(*args,**kwargs)    
admin.site.unregister(User)
admin.site.register(User,AccountsAdminUser)
admin.site.register(Home)
admin.site.register(Election_introduction)
admin.site.register(Party1)
admin.site.register(Vote_casting)
admin.site.register(Video)
