from flask import Flask
from utils import (
    env,
    error_hadler
)


app = Flask('CrowdTesting')
app.secret_key = env('SECRET_KEY')


@app.route('/', methods=['GET'])
@error_hadler
def mainpage():
    return {}, 200


if __name__ == '__main__':
    app.run(
        host=env('HOST'),
        port=env('PORT'),
        debug=env.bool('DEBUG'),
    )
