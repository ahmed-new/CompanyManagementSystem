from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=100)

    @property
    def number_of_departments(self):
        return self.department_set.count()

    @property
    def number_of_employees(self):
        return self.employee_set.count()

    @property
    def number_of_projects(self):
        return self.project_set.count()

    def __str__(self):
        return self.name


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    @property
    def number_of_employees(self):
        return self.employee_set.count()

    @property
    def number_of_projects(self):
        return self.project_set.count()

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=100)
    hired_on = models.DateField(null=True, blank=True)

    @property
    def days_employed(self):
        if self.hired_on:
            return (timezone.now().date() - self.hired_on).days
        return 0

    def __str__(self):
        return self.name


class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee, related_name="projects")

    def __str__(self):
        return self.name


class PerformanceReview(models.Model):
    REVIEW_STAGES = [
        ('Pending', 'Pending Review'),
        ('Scheduled', 'Review Scheduled'),
        ('Feedback', 'Feedback Provided'),
        ('Approval', 'Under Approval'),
        ('Approved', 'Review Approved'),
        ('Rejected', 'Review Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    stage = models.CharField(max_length=20, choices=REVIEW_STAGES, default='Pending')
    scheduled_date = models.DateField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.employee.name} - {self.stage}"

    def schedule_review(self, date):
        if self.stage == 'Pending':
            self.stage = 'Scheduled'
            self.scheduled_date = date
            self.save()
        else:
            raise ValueError("Cannot schedule review from the current stage.")

    def provide_feedback(self, feedback):
        if self.stage == 'Scheduled':
            self.stage = 'Feedback'
            self.feedback = feedback
            self.save()
        else:
            raise ValueError("Cannot provide feedback from the current stage.")

    def submit_for_approval(self):
        if self.stage == 'Feedback':
            self.stage = 'Approval'
            self.save()
        else:
            raise ValueError("Cannot submit for approval from the current stage.")

    def approve_review(self):
        if self.stage == 'Approval':
            self.stage = 'Approved'
            self.save()
        else:
            raise ValueError("Cannot approve from the current stage.")

    def reject_review(self):
        if self.stage == 'Approval':
            self.stage = 'Rejected'
            self.save()
        else:
            raise ValueError("Cannot reject from the current stage.")

    def resubmit_feedback(self):
        if self.stage == 'Rejected':
            self.stage = 'Feedback'
            self.save()
        else:
            raise ValueError("Cannot resubmit feedback from the current stage.")


class User(AbstractUser):
    ROLES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default='Employee')
