from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tests/test_config.py'  # Use banco de dados em memória para testes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
