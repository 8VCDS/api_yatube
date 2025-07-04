from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS доступно всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # разрешаем изменение только автору
        return obj.author == request.user
