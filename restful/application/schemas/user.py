
from marshmallow_sqlalchemy import ModelSchema

from application.models.db import db
from application.models.user import UserModel

class UserSchema(ModelSchema):
    class Meta:
        model = UserModel
        strict = True
        sqla_session = db.session