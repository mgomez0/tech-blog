import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ADMIN_PASSWORD = 'secret'
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
    DEBUG = False
    SECRET_KEY = 'shhh, secret!'  # Used by Flask to encrypt session cookie.
    SITE_WIDTH = 800

    