from django.contrib import admin
from .models import Testimony, Contact

# Register your models here.


class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname','is_approved', 'testimony_text', 'profile_picture']
    list_editable = ['is_approved','profile_picture']
    search_fields = ['fname', 'lname']
    list_filter = ['is_approved', 'fname', 'lname']
    
admin.site.register(Testimony, TestimonyAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','message']
    search_fields = ['name', 'email']
    list_filter = ['name', 'email']
    
admin.site.register(Contact, ContactAdmin)