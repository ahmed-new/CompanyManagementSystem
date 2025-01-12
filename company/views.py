from rest_framework import viewsets
from .models import Company, Department, Employee, Project, PerformanceReview
from .serializers import (
    CompanySerializer,
    DepartmentSerializer,
    EmployeeSerializer,
    ProjectSerializer,
    PerformanceReviewSerializer
)
from .permissions import IsAdmin, IsManager, IsEmployee




class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdmin]  # Only Admin can access all companies

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsManager]  # Only Manager can access departments related to their company

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsEmployee]  # Employees can access only their own data

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsManager]  # Managers can access projects in their department

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAdmin]  # Only Admin can manage performance reviews
