from .user import create_user
from .my_controllers import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()

