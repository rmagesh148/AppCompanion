from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from travelcompapp.models import UserDetails
from travelcompapp.serializers import UserDetailsSerializer

# Create your views here.

# Get List of Users and Create User
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        try:
            user_details_list = UserDetails.objects.all()
            if not user_details_list:
                return JsonResponse({'message' : 'User List is Empty'}, status = status.HTTP_204_NO_CONTENT)
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
    
# Get user based on guid
@api_view(['GET'])
def user(request):
    if request.method == 'GET':
        try:
            guid = request.GET.get('guid', None)
            if guid is not None:
                user_detail = UserDetails.objects.filter(guid=guid)
                if not user_detail:
                    return JsonResponse({'message' : 'User is not found'}, status=status.HTTP_204_NO_CONTENT)
                user_serializer = UserDetailsSerializer(user_detail, many=True)
                return JsonResponse(user_serializer.data, safe=False)
            return JsonResponse({'message' : 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message' : str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return JsonResponse({'message' : 'Home Page'}, status=status.HTTP_404_NOT_FOUND)