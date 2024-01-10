from rest_framework import permissions


class IsEmployer(permissions.BasePermission):
    """
    Custom permission to only allow employers to view the job applications.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the role 'employer'
        return request.user.is_authenticated and request.user.role == 'employer'


class IsCandidate(permissions.BasePermission):
    """
    Custom permission to only allow candidates to view the job applications.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the role 'candidate'
        return request.user.is_authenticated and request.user.role == 'candidate'

