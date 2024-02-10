import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_muito_dificil_de_adivinhar'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'aplicacao.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
