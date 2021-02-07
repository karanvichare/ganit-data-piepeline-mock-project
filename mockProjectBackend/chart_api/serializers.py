# Django rest framework related dependencies
from rest_framework import serializers

class CurrenyDataRequestSerializer(serializers.Serializer):
    """
    LoginRequestSerializer class defines the fields that get deserialized.
    """  
    currency = serializers.CharField(max_length=70)