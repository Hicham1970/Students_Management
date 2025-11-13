from django.contrib.auth.backends import ModelBackend
from django.core.cache import cache


class CachedModelBackend(ModelBackend):
    def get_user_permissions(self, user_obj, obj=None):
        """
        Return a set of permission strings the user `user_obj` has from their
        `user_permissions`.
        """
        cache_key = f'user_permissions_{user_obj.pk}'
        permissions = cache.get(cache_key)
        if permissions is None:
            permissions = super().get_user_permissions(user_obj, obj)
            # Cache for 5 minutes
            cache.set(cache_key, permissions, timeout=300)
        return permissions

    def get_group_permissions(self, user_obj, obj=None):
        """
        Return a set of permission strings the user `user_obj` has from the
        groups they belong.
        """
        cache_key = f'group_permissions_{user_obj.pk}'
        permissions = cache.get(cache_key)
        if permissions is None:
            permissions = super().get_group_permissions(user_obj, obj)
            # Cache for 5 minutes
            cache.set(cache_key, permissions, timeout=300)
        return permissions

    def get_all_permissions(self, user_obj, obj=None):
        """
        Return a set of permission strings the user `user_obj` has, including
        both user and group permissions.
        """
        cache_key = f'all_permissions_{user_obj.pk}'
        permissions = cache.get(cache_key)
        if permissions is None:
            permissions = super().get_all_permissions(user_obj, obj)
            # Cache for 5 minutes
            cache.set(cache_key, permissions, timeout=300)
        return permissions
