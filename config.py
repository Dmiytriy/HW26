class Config:
    DEBUG = True
    SECRET = "test"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_PRETTYPRINT_REGULAR = True
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}


