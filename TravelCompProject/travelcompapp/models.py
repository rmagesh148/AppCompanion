import uuid
from django.db import models

# Create your models here.
# Need to add active_user boolean.
class UserDetails(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guid = models.UUIDField(default=uuid.uuid4)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    picture_url = models.URLField(max_length=200, blank=True)
    phone_number = models.IntegerField(blank=True)
    email_id = models.EmailField(blank=False)
    created_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True, auto_now_add=False)
