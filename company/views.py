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
    permission_classes = [IsManager ,IsAdmin]

    def get_queryset(self):
   
        if self.request.user.role == 'Manager':
            return Department.objects.filter(manager=self.request.user)  
        
        return super().get_queryset()
    
      # Only Manager can access departments related to their company

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsEmployee ,IsAdmin ,IsManager]
    
    def get_queryset(self):
       
        if self.request.user.role == 'Employee':
            return Employee.objects.filter(id=self.request.user.id)  
        
        return super().get_queryset()  
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsManager,IsAdmin]  # Managers can access projects in their department

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAdmin ]  # Only Admin can manage performance reviews
