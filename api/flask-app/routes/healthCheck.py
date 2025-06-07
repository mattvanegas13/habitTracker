from flask import Blueprint
from healthcheck import HealthCheck

health_bp = Blueprint('health_bp', __name__)

@health_bp.route('/health-check')
def health_check():
    return HealthCheck().run()