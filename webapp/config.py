import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = 'kjuihkdfs7^nmnmvxzcvdsfsd$^345lk'

SQLALCHEMY_TRACK_MODIFICATIONS = False
