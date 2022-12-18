from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_genre(self, gid):
        return self.dao.get_by_genre(gid)

    def get_by_director(self, did):
        return self.dao.get_by_director(did)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create_movie(self, data):
        return self.dao.create_movie(data)

    def update(self, data):
        return self.dao.update(data)

    def delete(self, mid):
        self.dao.delete(mid)
