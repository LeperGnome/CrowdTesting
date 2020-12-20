from app import AppContext
from controllers.users import users_controller
from controllers.reports import reports_controller
from controllers.services import services_controller
from flask import Flask
from utils import (
    env,
    error_handler
)

app = AppContext.get_instance()
app.secret_key = env('SECRET_KEY')


# TODO: user loader


def add_controllers():
    app.flaskapp.register_blueprint(users_controller,
                                    url_prefix='api/users')
    app.flaskapp.register_blueprint(reports_controller,
                                    url_prefix='api/reports')
    app.flaskapp.register_blueprint(services_controller,
                                    url_prefix='api/services')


def runserver():
    add_controllers()
    print(app.flaskapp.url_map)
    app.flaskapp.run(
        host=env('HOST'),
        port=env('PORT'),
        debug=env.bool('DEBUG'),
    )


if __name__ == '__main__':
    runserver()
