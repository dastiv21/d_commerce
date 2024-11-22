from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit it.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsClient(permissions.BasePermission):
    """
    Custom permission to only allow clients to access the view.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated