import os

basedir = os.path.abspath(os.path.dirname(__file__))
APP_NAME = 'FlaskProject'
DEBUG = True
DATABASE_URL = fr"{basedir}/database/********.db"
PORT = 701
HOST = '127.0.0.1'
APP_SECRET_KEY = ''

SWAGGER_ENDPOINT = "/api/docs"
SWAGGER_API_URL = f"/swagger.json"
SWAGGER_CONFIG = {
    "app_name": "Flask project | API Doc",
    "layout": "BaseLayout",  # Options: "BaseLayout", "StandaloneLayout", "Topbar"
    "deepLinking": True,
    "displayOperationId": True,
    "defaultModelsExpandDepth": -1,
    "defaultModelRendering": "model",
}
