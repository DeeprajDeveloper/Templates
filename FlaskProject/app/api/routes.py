from typing import Union
from datetime import datetime
from flask import Blueprint, jsonify, request
from app.api import functionality as func

bp_api = Blueprint('bp_api', __name__, url_prefix='/api')


@bp_api.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200
