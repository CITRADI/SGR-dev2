import os

class Config:
    SECRET_KEY = 'citraditboard2023'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:citraditboard2023@localhost:5432/sgrdev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
