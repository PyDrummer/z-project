from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('driver', 'work_clock', 'drive_clock', 'work_status', 'drive_status')
        model = Driver