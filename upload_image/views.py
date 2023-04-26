from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TestUser
from .serializers import UserDataSerializer, UserImageSerializer


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def test_users(request):
    TestUser_get = TestUser.objects.all()
    serializer = UserDataSerializer(TestUser_get, many=True)

    return Response(serializer.data)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_users(request):
    # TestUser_get = TestUser.objects.all()
    serializer = UserDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=201)
    else:
        return Response(serializer.data, status=500)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def update_users(request, id):

    try:
        row = TestUser.objects.get(pk=id)
    except row.DoesNotExist:

        return Response({"message": "enter a bad id"}, status=500)

    serializer = UserDataSerializer(row, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=201)
    else:
        return Response(serializer.data, status=500)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['Delete'])
def delete_user(response, id):
    try:
        row = TestUser.objects.get(pk=id)
        row.delete()
        return Response("", status=204)
    except row.DoesNotExist:

        return Response({"message": "enter a bad id"}, status=404)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
# images
@api_view(['GET'])
def get_image(response):
    TestUser_get = TestUser.objects.all()
    serializer = UserImageSerializer(TestUser_get, many=True)

    return Response(serializer.data)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def update_image(request, id):
    try:
        row = TestUser.objects.get(pk=id)

    except row.DoesNotExist:

        return Response({"message": "enter a bad id"}, status=404)

    serializer = UserImageSerializer(row, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=201)
    else:
        return Response(serializer.data, status=500)
