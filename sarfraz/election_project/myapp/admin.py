from django.contrib import admin

# Register your models here.

from .models import Home,Election_introduction,Party1,Vote_casting,Video

# Register your models here.
admin.site.register(Home)
admin.site.register(Election_introduction)
admin.site.register(Party1)
admin.site.register(Vote_casting)
admin.site.register(Video)
