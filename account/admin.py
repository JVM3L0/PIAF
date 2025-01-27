from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("complete_name","username", "email", "birth_date", "contact") 
    search_fields = ("complete_name", "username", "email")  
    list_filter = ("complete_name", "username", "email", "birth_date")  


admin.site.register(Account, AccountAdmin)
