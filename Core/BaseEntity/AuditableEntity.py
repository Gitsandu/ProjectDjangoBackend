from django.db import models
import uuid
from datetime import datetime

class AuditableEntity(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.UUIDField(default=uuid.uuid4, editable=False)
    updated_by = models.UUIDField(default=uuid.uuid4, editable=False)
    updated_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
