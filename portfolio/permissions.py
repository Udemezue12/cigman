from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class ViewProfileHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('portfolio.view_history')
    
class ViewAuthorHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('portfolio.view_history')
    
class ViewAwardrHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('portfolio.view_history')
    
class ViewCertificateHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('portfolio.view_history')