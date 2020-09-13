# import os

class Config:
    """General configuration parent class"""
    # myAPIkey = os.environ.get('api_key')
    pass
    


class ProdConfig(Config):
    """Configuration for the  Production environment """

    pass


class DevConfig(Config):
    """Configuration for the development environment"""
    DEBUG = True

# config_options = {
#     'development':DevConfig, 
#     'production':ProdConfig
# }

