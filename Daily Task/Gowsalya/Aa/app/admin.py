from django.contrib import admin
from .models import EnqInsert
from .models import Subscription

admin.site.register(EnqInsert)
admin.site.register(Subscription)