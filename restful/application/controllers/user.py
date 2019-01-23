from application.models.user import UserModel
from application.models.db import db

class UserController(object):
    def __init__(self):
        self.model = UserModel

    def getUserByID(self, id):
        return self.model.query.filter_by(id=id).one_or_none()
    

    def getUsers(self):
        return self.model.query.all()

    def getUsersByName(self, name):
        if name:
            return self.model.query.filter_by(name=name).all()
        return None

    def updateUser(self):
        db.session.commit()

    def deleteUser(self, id):
        user = self.getUserByID(id)
        if user:
            db.session.delete(user)
            db.session.commit()

    def addUser(self, users):
        db.session.add_all(users)
        db.session.commit()