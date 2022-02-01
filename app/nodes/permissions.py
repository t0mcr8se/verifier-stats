from rest_framework import permissions
from .models import Whitelist


class WhitelistPermission(permissions.BasePermission):
    def has_permission(self, request, view=None):

        remote_addr = request.META["REMOTE_ADDR"]
        for entry in Whitelist.objects.all():
            valid_ip = entry.ip_address
            if remote_addr == valid_ip:
                return True

        return False
