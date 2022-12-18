from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def create_movie(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, data):
        mid = data.get('id')

        self.session.query(Movie).filter(Movie.id == mid).update(data)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
