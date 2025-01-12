from django.test import TestCase
from django.utils import timezone
from .models import Company, Department, Employee, Project

class CompanyModelTests(TestCase):

    def setUp(self):
       
        self.company = Company.objects.create(name="My Company")
        
       
        self.department = Department.objects.create(name="Engineering", company=self.company)

    def test_number_of_departments(self):
       
        department = Department.objects.create(name="HR", company=self.company)
        
        
        self.assertEqual(self.company.number_of_departments, 2)

    def test_number_of_employees(self):
        
        employee = Employee.objects.create(
            name="John Doe", 
            email="johndoe@example.com", 
            mobile_number="1234567890",
            address="123 Main St", 
            designation="Engineer", 
            hired_on="2020-01-01", 
            company=self.company, 
            department=self.department
        )

        
        self.assertEqual(self.company.number_of_employees, 1)

    def test_number_of_projects(self):
       
        project = Project.objects.create(
            name="Project A", 
            description="A test project",
            start_date=timezone.now().date(), 
            end_date=timezone.now().date(),
            company=self.company, 
            department=self.department
        )
        
        
        self.assertEqual(self.company.number_of_projects, 1)


class DepartmentModelTests(TestCase):

    def setUp(self):
        
        self.company = Company.objects.create(name="My Company")
        
        
        self.department = Department.objects.create(name="Engineering", company=self.company)

    def test_number_of_employees(self):
        
        employee = Employee.objects.create(
            name="John Doe", 
            email="johndoe@example.com", 
            mobile_number="1234567890",
            address="123 Main St", 
            designation="Engineer", 
            hired_on="2020-01-01", 
            company=self.company, 
            department=self.department
        )
        
        
        self.assertEqual(self.department.number_of_employees, 1)

    def test_number_of_projects(self):
        
        project = Project.objects.create(
            name="Project A", 
            description="A test project", 
            start_date=timezone.now().date(), 
            end_date=timezone.now().date(),
            company=self.company, 
            department=self.department
        )
        
        
        self.assertEqual(self.department.number_of_projects, 1)


class EmployeeModelTests(TestCase):

    def setUp(self):
        
        self.company = Company.objects.create(name="My Company")
        
        
        self.department = Department.objects.create(name="Engineering", company=self.company)

        
        self.employee = Employee.objects.create(
            name="John Doe", 
            email="johndoe@example.com", 
            mobile_number="1234567890",
            address="123 Main St", 
            designation="Engineer", 
            hired_on="2020-01-01", 
            company=self.company, 
            department=self.department
        )

    def test_days_employed(self):
        
        self.assertEqual(self.employee.days_employed, (timezone.now().date() - self.employee.hired_on).days)


class ProjectModelTests(TestCase):

    def setUp(self):
        
        self.company = Company.objects.create(name="My Company")
        
        
        self.department = Department.objects.create(name="Engineering", company=self.company)

        
        self.employee = Employee.objects.create(
            name="John Doe", 
            email="johndoe@example.com", 
            mobile_number="1234567890",
            address="123 Main St", 
            designation="Engineer", 
            hired_on="2020-01-01", 
            company=self.company, 
            department=self.department
        )

       
        self.project = Project.objects.create(
            name="Project A", 
            description="A test project", 
            start_date=timezone.now().date(), 
            end_date=timezone.now().date(),
            company=self.company, 
            department=self.department
        )

        
        self.project.assigned_employees.add(self.employee)

    def test_assigned_employees(self):
        
        self.assertEqual(self.project.assigned_employees.count(), 1)
        self.assertEqual(self.project.assigned_employees.first(), self.employee)
