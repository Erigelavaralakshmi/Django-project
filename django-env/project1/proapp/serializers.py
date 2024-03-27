from proapp.models import Employee, Department
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from rest_framework import status

class BaseSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class EmployeeSerializer(BaseSerializer):
    class Meta:
        model = Employee
        fields = BaseSerializer.Meta.fields + ['name', 'id_number', 'date_of_joining','salary','active']

class DepartmentSerializer(BaseSerializer):
    class Meta:
        model = Department
        fields = BaseSerializer.Meta.fields + ['name', 'date_of_creation', 'employee_count', 'active']
        