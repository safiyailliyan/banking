from django.contrib import admin
from . models import transaction
from . models import team
# Register your models here.
admin.site.register(transaction)
admin.site.register(team)