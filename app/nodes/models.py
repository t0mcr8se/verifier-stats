from django.db import models, connection
from django.utils.translation import gettext as _
from django.core.management.color import no_style


class Node(models.Model):
    @classmethod
    def truncate(cls):
        sequence_sql = connection.ops.sequence_reset_sql(
            no_style(),
            [
                Node,
            ],
        )
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))
            for sql in sequence_sql:
                cursor.execute(sql)
            connection.commit()

    ip_address = models.GenericIPAddressField(_("Node IP Address"), protocol="IPv4")
    last_block = models.IntegerField(_("Node Last Block"))

    class Meta:
        verbose_name = _("Node")
        verbose_name_plural = _("Nodes")

    def __str__(self):
        return self.name


class Whitelist(models.Model):

    ip_address = models.GenericIPAddressField(_("IP Address"), protocol="IPv4")

    class Meta:
        verbose_name = _("Whitelist")
        verbose_name_plural = _("Whitelist")

    def __str__(self):
        return self.ip_address
