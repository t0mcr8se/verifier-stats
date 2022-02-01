from rest_framework import serializers
from .models import Node
from .permissions import WhitelistPermission
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)


class MaskedIPAddressField(serializers.IPAddressField):
    def to_representation(self, value):
        if WhitelistPermission().has_permission(self.context["request"]):
            return super().to_representation(value)
        ip_list = value.split(".")
        masked_ip = f"{ip_list[0]}.*.*.{ip_list[3]}"
        return masked_ip


class NodeSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    ip_address = MaskedIPAddressField()
    # uncomment the line below to keep same ids
    # id = serializers.IntegerField()

    class Meta:
        model = Node
        fields = "__all__"
        list_serializer_class = BulkListSerializer
