# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from pathlib import Path

class Config(object):

    BASE_DIR = Path(__file__).resolve().parent
    
    USERS_ROLES  = { 'ADMIN'  :1 , 'USER'      : 2 }
    USERS_STATUS = { 'ACTIVE' :1 , 'SUSPENDED' : 2 }
    
    # celery 
    CELERY_BROKER_URL     = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    CELERY_HOSTMACHINE    = "celery@app-generator"

    # Set up the App SECRET_KEY
    SECRET_KEY  = os.getenv('SECRET_KEY', 'S3cret_999')

    # Social AUTH context
    SOCIAL_AUTH_GITHUB  = False

    GITHUB_ID      = os.getenv('GITHUB_ID'    , None)
    GITHUB_SECRET  = os.getenv('GITHUB_SECRET', None)

    # Enable/Disable Github Social Login    
    if GITHUB_ID and GITHUB_SECRET:
         SOCIAL_AUTH_GITHUB  = True    

    GOOGLE_ID      = os.getenv('GOOGLE_ID'    , None)
    GOOGLE_SECRET  = os.getenv('GOOGLE_SECRET', None)

    # Enable/Disable Google Social Login    
    if GOOGLE_ID and GOOGLE_SECRET:
         SOCIAL_AUTH_GOOGLE  = True    

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
    DB_USERNAME = os.getenv('DB_USERNAME' , None)
    DB_PASS     = os.getenv('DB_PASS'     , None)
    DB_HOST     = os.getenv('DB_HOST'     , None)
    DB_PORT     = os.getenv('DB_PORT'     , None)
    DB_NAME     = os.getenv('DB_NAME'     , None)

    USE_SQLITE  = True 

    # try to set up a Relational DBMS
    if DB_ENGINE and DB_NAME and DB_USERNAME:

        try:
            
            # Relational DBMS: PSQL, MySql
            SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
                DB_ENGINE,
                DB_USERNAME,
                DB_PASS,
                DB_HOST,
                DB_PORT,
                DB_NAME
            ) 

            USE_SQLITE  = False

        except Exception as e:

            print('> Error: DBMS Exception: ' + str(e) )
            print('> Fallback to SQLite ')    

    if USE_SQLITE:

        # This will create a file in <app> FOLDER
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

    DYNAMIC_DATATB = {
        "products": "apps.models.Product"
    }

    CDN_DOMAIN = os.getenv('CDN_DOMAIN')
    CDN_HTTPS = os.getenv('CDN_HTTPS', True)

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
