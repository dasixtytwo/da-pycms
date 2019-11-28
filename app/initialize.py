from app.config import config
from app.controllers.userController import UserController
from app.password import get_hashed_password


def add_user():
    if UserController.get(name=config['username']):
        return

    user = UserController.create(
        name=config['username'],
        password=get_hashed_password(config['password'])
    )

    print('Created user: {}'.format(str(user.id)))


def init():
    add_user()
