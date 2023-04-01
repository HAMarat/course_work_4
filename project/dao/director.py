from project.dao.base import BaseDAO
from project.dao.model.director import Director


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director
