import os

class Config:
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False