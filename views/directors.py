from flask_restx import Resource, Namespace

from container import director_service
from dao.models.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorViews(Resource):
    def get(self):
        query = director_service.get_directors()
        return directors_schema.dump(query)


@director_ns.route("/<int:did>")
class DirectorViews(Resource):
    def get(self, did):
        query = director_service.get_director(did)
        answer = director_schema.dump(query)

        if len(answer) == 0:
            return 'таких режиссеров нет'

        return answer, 200

