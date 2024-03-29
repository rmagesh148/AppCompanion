from django.utils.dateparse import parse_date
from django.http.response import JsonResponse
from django.db.models import Count

from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.decorators import api_view

from travelcompapp.models import UserDetails, PassengerTravelInfo
from travelcompapp.serializers import UserDetailsSerializer, PassengerTravelInfoSerializer, PassengerGroupBySerializer, AirportCitySerializer, PassengerInfoSerializer


@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return JsonResponse({'message' : 'Home Page'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        try:
            user_details_list = UserDetails.objects.all()
            if not user_details_list:
                return JsonResponse({'message': 'User List is Empty'}, status=status.HTTP_204_NO_CONTENT)
            user_list_serializer = UserDetailsSerializer(user_details_list, many=True)
            return JsonResponse(user_list_serializer.data, safe=False)
        except UserDetails.DoesNotExist:
            return JsonResponse({'message': 'There is some error'}, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'POST':
        user_detail = JSONParser().parse(request)
        user_serializer = UserDetailsSerializer(data=user_detail)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user(request):
    """
    Get User based on the guid
    :param request: guid
    :return: User Serializer object
    """
    if request.method == 'GET':
        try:
            guid = request.GET.get('guid', None)
            if guid is not None:
                user_detail = UserDetails.objects.filter(guid=guid)
                if not user_detail:
                    return JsonResponse({'message': 'User is not found'}, status=status.HTTP_204_NO_CONTENT)
                user_serializer = UserDetailsSerializer(user_detail, many=True)
                return JsonResponse(user_serializer.data, safe=False)
            return JsonResponse({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def travel_info_create_get(request):
    if request.method == 'POST':
        try:
            travel_info = JSONParser().parse(request)
            travel_info_serializer = PassengerTravelInfoSerializer(data=travel_info)
            if travel_info_serializer.is_valid():
                travel_info_serializer.save()
                return JsonResponse(travel_info_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(travel_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            flight_no = request.GET.get('flight_no', None)
            if flight_no is not None:
                travel_info = PassengerTravelInfo.objects.filter(flight_no=flight_no)
                if not travel_info:
                    return JsonResponse({'message': 'Travel Info is not found'}, status=status.HTTP_204_NO_CONTENT)
                travel_info_serializer = PassengerTravelInfoSerializer(travel_info, many=True)
                print(travel_info_serializer.data)
                return JsonResponse(travel_info_serializer.data, safe=False)
            return JsonResponse({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_info_group_flight_no(request):
    try:
        if request.method == 'GET':
            travel_list = []
            from_range_date = request.GET.get('from_range_date', None)
            to_range_date = request.GET.get('to_range_date', None)
            arr_airport_code = request.GET.get('arr_airport_code', None)
            dep_airport_code = request.GET.get('dep_airport_code', None)

            if arr_airport_code is not None and dep_airport_code is not None:
                filtered_objects = (PassengerTravelInfo.objects
                                    .filter(arr_airport_code=arr_airport_code, dep_airport_code=dep_airport_code))
            else:
                return JsonResponse({'message': 'Arr/Dep Input is missing'}, status=status.HTTP_400_BAD_REQUEST)
            
            if from_range_date is not None and to_range_date is None:
                travel_list = (filtered_objects.filter(travel_date=parse_date(from_range_date))
                               .values('flight_no', 'airlines', 'arr_airport_code',
                                       'dep_airport_code', 'status_of_ticket', 'travel_date')
                               .annotate(count=Count('flight_no')))
            
            elif from_range_date is not None and to_range_date is not None:
                travel_list = (filtered_objects
                               .filter(travel_date__range=[parse_date(from_range_date), parse_date(to_range_date)])
                               .values('flight_no', 'airlines', 'arr_airport_code',
                                       'dep_airport_code', 'status_of_ticket', 'travel_date')
                               .annotate(count=Count('flight_no')))
            if not travel_list:
                return JsonResponse({'message': 'Result set is Empty'}, status=status.HTTP_204_NO_CONTENT)
            travel_serializer = (PassengerGroupBySerializer(travel_list, many=True))
            return JsonResponse(travel_serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_airport_city(request):
    try:
        if request.method == 'GET':
            # search_query = request.GET.get('search_query',None)
            output = [{"airport_city": "Chennai", "airport_iata": "MAA"},
                      {"airport_city": "New York", "airport_iata": "NYC"},
                      {"airport_city": "DC", "airport_iata": "IAD"},
                      {"airport_city": "Atlanta", "airport_iata": "ATL"}]
            if output is not None:
                output_serializer = AirportCitySerializer(output, many = True)
                return JsonResponse(output_serializer.data, safe=False)
            else:
                return JsonResponse({'message': 'Result set is Empty'}, status=status.HTTP_204_NO_CONTENT)
        else:
            print("failure")
    except Exception as e:
        print(e)


@api_view(['GET'])
def get_travelers_info(request):
    try:
        if request.method == 'GET':
            flight_no = request.GET.get('flight_no', None)
            travel_date = request.GET.get('travel_date', None)

            if flight_no is not None and travel_date is not None:
                travel_info_list = PassengerTravelInfo.objects.filter(travel_date=parse_date(travel_date),
                                                                      flight_no=flight_no)
                print(travel_info_list)
                print(travel_info_list)
                user_info = UserDetails.objects.filter(user_id = travel_info_list[''])

            else:
                return JsonResponse({'message' : 'Input is missing'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
