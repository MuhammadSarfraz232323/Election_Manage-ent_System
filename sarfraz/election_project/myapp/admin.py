from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import Home,Election_introduction,Party1,Vote_casting,Video
from django.contrib.auth.admin import UserAdmin as AuthAdminUser
from myapp.models import UserProfile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
class UserProfileInlines(admin.StackedInline):
    model=UserProfile
    can_delete=False

class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self,*args,**kwargs):
        self.inlines=[]
        return super(AccountsUserAdmin,self).add_view(*args,**kwargs)
    def change_view(self,*args,**kwargs):
        self.inlines=[UserProfileInlines]
        return super(AccountsUserAdmin,self).change_view(*args,**kwargs)    
admin.site.unregister(User)
admin.site.register(User,AccountsUserAdmin)      
admin.site.register(Home)
admin.site.register(Election_introduction)
admin.site.register(Party1)
admin.site.register(Vote_casting)
admin.site.register(Video)
