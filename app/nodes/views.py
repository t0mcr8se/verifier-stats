from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from .serializers import NodeSerializer
from .models import Node
from .permissions import WhitelistPermission
from rest_framework_bulk import BulkCreateModelMixin


class NodeViewset(BulkCreateModelMixin, mixins.DestroyModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                permissions.AllowAny,
            ]
        else:
            self.permission_classes = [
                WhitelistPermission,
            ]
        return super(NodeViewset, self).get_permissions()

    def perform_bulk_create(self, serializer):
        Node.truncate()
        return super().perform_bulk_create(serializer)
