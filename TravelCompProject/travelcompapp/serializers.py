from rest_framework import serializers
from travelcompapp.models import UserDetails, PassengerTravelInfo

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = ('guid',
                    'first_name',
                    'last_name',
                    'picture_url',
                    'phone_number',
                    'email_id' )

class PassengerTravelInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassengerTravelInfo
        fields = ('guid',
                    'passenger_user_id',
                    'flight_no',
                    'airlines',
                    'arr_arline_code',
                    'dep_arline_code',
                    'status_of_ticket',
                    'travel_date',
                    'comments')

class PassengerGroupBySerializer(serializers.Serializer):
    
    count = serializers.IntegerField()
    flight_no = serializers.CharField(max_length=100)
    airlines = serializers.CharField(max_length=100)
    arr_arline_code = serializers.CharField(max_length=100)
    dep_arline_code = serializers.CharField(max_length=100)
    travel_date = serializers.DateField()
    status_of_ticket = serializers.BooleanField()
    comments = serializers.CharField(max_length=200)
