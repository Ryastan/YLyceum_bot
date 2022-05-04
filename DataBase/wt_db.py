import datetime
import sqlalchemy
from db_session import SqlAlchemyBase


class WT_users(SqlAlchemyBase):
    __tablename__ = 'WT_users'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    discord_id = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True, index=True)
    room_id = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)


