from djongo import models
from rest_framework import serializers
from timeTracking.models import Attendances

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendances
        fields = '__all__'
        