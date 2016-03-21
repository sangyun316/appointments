"""
    Database Initialization File

    This file takes the configurations from the database configuration file and creates the "db" object
    The "db" object can be used by all of the models to interact with the database
"""
from app.config import database
import importlib
import os

def _get_config(env):
    return {
        'DEVELOPMENT': database.DevelopmentDBConfig,
        'STAGING': database.StagingDBConfig,
        'PRODUCTION': database.ProductionDBConfig,
    }.get(env, database.DevelopmentDBConfig)

def init_db(app):
    config = _get_config(os.getenv('PYLOT_ENV', 'DEVELOPMENT'))

    if config.DB_ON:
        driver_file = 'system.db.drivers._' + config.DB_DRIVER
        db_connector = importlib.import_module(driver_file)
        #TODO: FIX THIS
        if not db_connector:
            raise Exception('Right now we do not have support for #{driver_file}') # fix this 
        app.config['SQLALCHEMY_ECHO'] = True
        db = db_connector.connect(config, app)
        app.db = db

