from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to check if the requester
    is the owner
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsStaffOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    Custom permission to check if the requester
    is a staff member
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsStaffOrOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to check if the requester
    is the owner or staff member
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff
