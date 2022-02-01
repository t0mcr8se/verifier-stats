from django.contrib import admin

from .models import Node, Whitelist

admin.site.register(Node)
admin.site.register(Whitelist)
