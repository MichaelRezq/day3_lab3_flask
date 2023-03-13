
import os
## developemt , production
class Config:
    SECRET_KEY = os.urandom(32)
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "postgresql://rowida_nageh:root@localhost:5432/rowida"



class ProductionConfig(Config):
    DEBUG= False
    # postgresql:://username:password@localhost:portnumber/dbname
    SQLALCHEMY_DATABASE_URI = "postgresql://rowida_nageh:root@localhost:5432/rowida"



projectConfig= {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}
# dbuser = 'crowd_user'
# dbpassword = 'root'
# dbname = 'crowd_funding_console_app'

