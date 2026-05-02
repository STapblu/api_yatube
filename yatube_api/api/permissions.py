from rest_framework import permissions  # type:ignore


class IsAuthenticatedOwnerOrReadOnly(permissions.BasePermission):
    """
    Доступ только для аутентифицированных пользователей.
    Изменение/удаление разрешено только владельцу объекта.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        owner_field = getattr(view, 'owner_field', 'author')
        owner = getattr(obj, owner_field, None)

        return owner == request.user
