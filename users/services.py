from users.models import User


class UserService:
    @staticmethod
    def create(data: dict):
        User.objects.create(**data)
