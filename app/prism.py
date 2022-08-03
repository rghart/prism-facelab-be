import logging

from flask import Flask
from app.webhooks.blvd import appointment_created, client_created

logging.basicConfig(level=logging.INFO)
logging.getLogger('werkzeug').setLevel(logging.INFO)

app = Flask(__name__)

app.register_blueprint(appointment_created.blueprint)
app.register_blueprint(client_created.blueprint)


@app.route('/')
def index():
    return 'Prism BE'


if __name__ == '__main__':
    app.run(port=5000)
