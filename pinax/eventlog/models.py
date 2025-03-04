from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from .signals import event_logged

try:  # Very ugly style, but we need to get JSONField some how
    from django.contrib.postgres.fields import JSONField
except ImportError:  # Postgres
    try:
        from django_mysql.models import JSONField
    except ImportError:  # MySQL
        try:
            from django_extensions.db.fields.json import JSONField
        except ImportError:  # Django extensions which is great!
            try:
                from jsonfield import JSONField
            except ImportError:  # Last but not least!
                print("Please install a jsonfield dependency")


class Log(models.Model):
    user = models.ForeignKey(
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        null=True,
        on_delete=models.SET_NULL
    )
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
    object_id = models.PositiveIntegerField(null=True)
    obj = GenericForeignKey("content_type", "object_id")
    extra = JSONField()

    @property
    def template_fragment_name(self):
        return "pinax/eventlog/{}.html".format(self.action.lower())

    class Meta:
        ordering = ["-timestamp"]


def log(user, action, extra=None, obj=None, dateof=None):
    if (user is not None and not user.is_authenticated):
        user = None
    if extra is None:
        extra = {}
    content_type = None
    object_id = None
    if obj is not None:
        content_type = ContentType.objects.get_for_model(obj)
        object_id = obj.pk
    if dateof is None:
        dateof = timezone.now()

    event = Log.objects.create(
        user=user,
        action=action,
        extra=extra,
        content_type=content_type,
        object_id=object_id,
        timestamp=dateof
    )
    event_logged.send(sender=Log, event=event)
    return event
