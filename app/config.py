import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'

    UPLOAD_FOLDER = './app/static/uploads'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://project1:Shawn20@localhost/project1'
    SQLALCHEMY_DATABASE_URI = 'postgresql://lewpdcgeglycdn:8f9e24c6e5bf109a13747876b6f8ddd169e5e8a98b86c3890b2cf4a4ad0ecc9b@ec2-54-196-33-23.compute-1.amazonaws.com:5432/dcea90b488ao31'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False