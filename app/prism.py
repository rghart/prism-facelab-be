from flask import Flask
from app.webhooks import blvd_appointment_created

app = Flask(__name__)

app.register_blueprint(blvd_appointment_created.blueprint)


@app.route('/')
def index():
    return 'Prism BE'


if __name__ == '__main__':
    app.run(port=5000)
