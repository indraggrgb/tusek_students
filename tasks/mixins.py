from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance= self.get_object()
        if instance.creator != self.request.user:
            raise PermissionDenied("You do not have permission to edit this task.")
        return super().dispatch(request, *args, **kwargs)