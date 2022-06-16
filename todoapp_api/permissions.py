from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyAuthorEdit(BasePermission):
    """ Проверка авторства заметки"""
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS: # Если хотим только читать
            return True
        return request.user == obj.author   # Если хотим редактировать


class OnlyPublicRead(BasePermission):
    """ Проверка публичности записи"""
    def has_object_permission(self, request, view, obj):
        if obj.public:
            return True
        return request.user == obj.author


class OnlyPublicComment(BasePermission):
    """ Проверка всех публичных записей для комментариев"""
    def has_object_permission(self, request, view, obj):
        if request.comment_note == obj.public:
            return True
        return False



