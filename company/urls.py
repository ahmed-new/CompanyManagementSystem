from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, DepartmentViewSet, EmployeeViewSet, ProjectViewSet
from .views import PerformanceReviewViewSet
from rest_framework.authtoken.views import obtain_auth_token





router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'projects', ProjectViewSet)

router.register(r'performance-reviews', PerformanceReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
