from shorty.app import create_app
from flask_swagger_ui import get_swaggerui_blueprint

app = create_app()

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Shorty"
    },
)

app.register_blueprint(swaggerui_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
