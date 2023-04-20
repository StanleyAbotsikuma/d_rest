from rest_framework import serializers
from .models import TestUser

class UserDataSerializer(serializers.ModelSerializer):

  class Meta:
    model = TestUser
    fields = ["id","name","password","randoms"]

class UserImageSerializer(serializers.ModelSerializer):

  class Meta:
    model = TestUser
    fields = ["id","upload"]