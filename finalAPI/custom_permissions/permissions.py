from rest_framework.permissions import BasePermission


class IsManager(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_authenticated
        else:
            return request.user.groups.filter(name='Manager').exists()
