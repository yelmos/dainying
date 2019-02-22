import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '111'



class DevelopConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'develop.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:0000@127.0.0.1:3306/kaosi'

config = {
    'develop': DevelopConfig,
    'default': DevelopConfig,
}


def init_app(app,env_name):
    app.config.from_object(config.get(env_name))

