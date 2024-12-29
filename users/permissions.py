from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Класс для проверки прав доступа для владельца
    """

    def has_object_permission(self, request, object,  view):
        """
        Проверяет, является ли пользователь владельцем
        """
        if object.author == request.user:
            return True
        return False


class IsAdmin(BasePermission):
    """
    Проверка прав доступа для пользователей с ролью "admin"
    """

    def has_permission(self, request, view):
        """
        Проверяет роль пользователя
        """
        return request.user.role == "admin"
