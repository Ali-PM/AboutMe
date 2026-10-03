from django.contrib import admin

import ContactUsapp
from .models import ContactUs, MassageMe

# Register your models here.

admin.site.register(ContactUs)
admin.site.register(MassageMe)