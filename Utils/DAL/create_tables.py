from .Models.models import User


def create_tables():
    user_service = User()
    user_service.createTable()
