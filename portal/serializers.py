from rest_framework import serializers
from .models import *

class persinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=persinfo
        fields = "__all__"