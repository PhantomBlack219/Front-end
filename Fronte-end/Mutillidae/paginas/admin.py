from django.contrib import admin

# Register your models here.
from .models import Owasp, Aindice

admin.site.register(Owasp)
admin.site.register(Aindice)
