import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'

    UPLOAD_FOLDER = './app/static/uploads'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://project1:Shawn20@localhost/project1'
    SQLALCHEMY_DATABASE_URI = 'postgresql://fguowfgymgevsm:8923c4e4c81b3e94920dbcf2e36940593328815e1fed50caf13090786b0b7ca9@ec2-54-83-46-116.compute-1.amazonaws.com:5432/da2gco69j5rfpi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False