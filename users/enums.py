from enum import Enum


class UserTypes(Enum):
    USER = 1
    ADMIN = 2

    @classmethod
    def access_types(cls):
        return [
            cls.USER.value,
            cls.ADMIN.value
        ]
