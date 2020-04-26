from django.contrib import admin

# Register your models here.
from .models import Host, Event


admin.site.register(Host)
admin.site.register(Event)
