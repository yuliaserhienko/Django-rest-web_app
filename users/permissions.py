from rest_framework.permissions import BasePermission
from .enums import UserTypes


class GetUserMixin:

    @staticmethod
    def get_user(view):
        _user = None
        lookup_url_kwarg = view.lookup_url_kwarg or view.lookup_field
        if lookup_url_kwarg in view.kwargs:
            _user = view.get_object()
        return _user


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return getattr(request.user, 'type', None) == UserTypes.ADMIN.value


class IsUserAccount(GetUserMixin, BasePermission):

    def has_permission(self, request, view):
        return request.user == self.get_user(view)


class IsAdminOrUserAccount(GetUserMixin, BasePermission):

    def has_permission(self, request, view):
        return any([
            request.user == self.get_user(view),
            getattr(request.user, 'type', None) == UserTypes.ADMIN.value
        ])
