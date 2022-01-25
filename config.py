import os
basedir = os.path.abspath(os.path.dirname(__file__)) #directory of current file

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #secret key to prevent CSRF attacks 'seasurf'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') #location of db 
    SQLALCHEMY_TRACK_MODIFICATIONS = False #notify application everytime a change is about to be made to the db= false
    
