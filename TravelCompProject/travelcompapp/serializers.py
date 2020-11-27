from rest_framework import serializers
from travelcompapp.models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = ('guid',
                    'first_name',
                    'last_name',
                    'picture_url',
                    'phone_number',
                    'email_id' )