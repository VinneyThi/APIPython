from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        extra_kargs = {
            'email' : {'write_only': True}
        }
        fields = [
            'name',
            'email',
            'department']
    