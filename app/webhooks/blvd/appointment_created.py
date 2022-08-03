from flask import Blueprint

blueprint = Blueprint('blvd_appointment_created', __name__, url_prefix='/blvd')


@blueprint.route('/appointment_created')
def appointment_created():
    return 'Appointment created!'
