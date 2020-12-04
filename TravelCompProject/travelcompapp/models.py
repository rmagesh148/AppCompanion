import uuid
from django.db import models

# Create your models here.
# Need to add active_user boolean.


class UserDetails(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guid = models.UUIDField(default=uuid.uuid4)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    picture_url = models.URLField(blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email_id = models.EmailField(blank=False)
    created_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True, auto_now_add=False)


class PassengerTravelInfo(models.Model):
    guid = models.UUIDField(default=uuid.uuid4)
    primary_guid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    passenger_user_id = models.CharField(max_length=100, blank=False)
    flight_no = models.CharField(max_length=100)
    airlines = models.CharField(max_length=200)
    arr_arline_code = models.CharField(max_length=100)
    dep_arline_code = models.CharField(max_length=100)
    travel_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    no_of_adults = models.IntegerField(blank=True, null=True)
    no_of_kids = models.IntegerField(blank=True, null=True)
    status_of_ticket = models.BooleanField(blank=False)
    comments = models.TextField()
    created_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True, auto_now_add=False)


class RequestStore(models.Model):
    guid = models.UUIDField(default=uuid.uuid4)
    primary_guid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    from_user_id = models.CharField(max_length=100, blank=False)
    to_user_id = models.CharField(max_length=100, blank=False)
    request_status = models.CharField(max_length=20, blank=False)
    flight_no = models.CharField(max_length=100)
    request_note = models.TextField()
    travel_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    created_date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True, auto_now_add=False)




