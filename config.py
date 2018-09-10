import os

class Config:
  
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://protus:suzy2015@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

       #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'One Minute Pitch'
    SENDER_EMAIL = 'protus.bantan@gmail.com'

  

class ProdConfig(Config):
      '''
  This is the production configuration child class

  Args:
      Config: The parent configuration class with the general config settings
  '''

      SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_COPPER_URL")

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://protus:suzy2015@localhost/pitch'

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'test':TestConfig
}