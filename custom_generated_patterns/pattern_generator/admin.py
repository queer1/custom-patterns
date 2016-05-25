from django.contrib import admin
from .models import measurements
from .models import pattern

admin.site.register(measurements)

admin.site.register(pattern)