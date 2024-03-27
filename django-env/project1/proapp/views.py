from rest_framework import mixins
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


class Employeeviewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Employee.objects.filter(active = True)
    serializer_class = EmployeeSerializer

class Departmentviewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

router = DefaultRouter()
router.register("employee", Employeeviewset, basename = "employee")
router.register("department", Departmentviewset, basename="department")

