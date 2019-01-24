from application.models.db import db
from sqlalchemy import Enum
import datetime
import sys

class UserModel(db.Model):
    __tablename__ = 'tbl_user'
    
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(60), nullable = False)
    birth = db.Column(db.Date, nullable = False)
    gender = db.Column(db.Enum("MALE", "FEMALE", native_enum = False), nullable = False)

