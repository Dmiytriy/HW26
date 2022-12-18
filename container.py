from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from services.director import DirectorService
from services.genre import GenreService
from services.movie import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
