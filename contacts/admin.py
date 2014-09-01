from django.contrib import admin

# Register your models here.
from contacts.models import Person, UserProfile

class PersonAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'first_name', 'second_name', 'last_name', 'phone', 'email')

admin.site.register(Person, PersonAdmin)