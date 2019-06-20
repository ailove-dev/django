from django.contrib.auth import get_user_model

User = get_user_model()


class BusinessClassBackend:
    @staticmethod
    def authenticate(request, username=None, password=None):
        if username is None:
            return

        try:
            user = User.objects.get(username=username)
            if user.is_staff:
                return None
        except User.DoesNotExist:
            user = User(username=username)
            user.set_unusable_password()
            user.save()

        return user

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
