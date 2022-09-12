from django.contrib import admin
from app1.models import *

# Register your models here.
@admin.register(Students)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','courses','jdate']

