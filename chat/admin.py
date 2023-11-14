from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "type", "date_time", "date_updated"]
    list_filter = ["name", "email", "type", "date_time"]
    search_fields =["name", "email"]
    list_editable = ["name", "type"]


admin.site.register(Contact, ContactAdmin)
