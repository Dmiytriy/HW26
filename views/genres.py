from flask_restx import Resource, Namespace

from container import genre_service
from dao.models.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreViews(Resource):
    def get(self):
        query = genre_service.get_genres()
        return genres_schema.dump(query)


@genre_ns.route("/<int:gid>")
class GenreViews(Resource):
    def get(self, gid: int):
        query = genre_service.get_genre(gid)
        answer = genre_schema.dump(query)

        if len(answer) == 0:
            return 'таких жанров нет'

        return answer, 200
