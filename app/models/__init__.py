from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


# Inheriting the declarative base model
class BaseModel(db.Model):

    __abstract__ = True

    id_ = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    created_at = db.Column(db.DateTime(), server_default=func.now())
