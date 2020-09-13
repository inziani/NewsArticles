from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
# from config import config_options

#  Initializing the application and creating the configs
# def create_app(config_name):
app = Flask(__name__)

# # Setting up the configuration
app.config.from_object(DevConfig)

  # # Registering the Blueprints
  # from .main import main as main_blueprint
  # app.register_blueprint(main_blueprint)

  # return app

#initializing Flask extensions
bootstrap = Bootstrap(app)


from .main import views



