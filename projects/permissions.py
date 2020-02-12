from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    # Only User edits persoanl profile

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnContent(permissions.BasePermission):
    # Only User update persoanl content
    def has_object_permission(self, request, view, obj):
        # Confirm it's user trying to update content
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
