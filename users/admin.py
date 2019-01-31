
from django.contrib import admin
#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site



class CustomUserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username','id','email' ]

admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.register(CustomUser, CustomUserAdmin)