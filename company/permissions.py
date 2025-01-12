from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Only Admin has access to all the data
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Admin'


class IsManager(permissions.BasePermission):
    """
    Only Manager has access to data for his/her department
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Manager'


class IsEmployee(permissions.BasePermission):
    """
    Only Employee can access their own data
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Employee'
