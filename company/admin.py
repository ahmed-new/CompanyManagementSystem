from django.contrib import admin
from .models import Company,Employee,Project,Department,PerformanceReview ,User

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(PerformanceReview)
admin.site.register(User)


