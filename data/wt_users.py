import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class WT_user(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    discord_id = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    streamkey = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
