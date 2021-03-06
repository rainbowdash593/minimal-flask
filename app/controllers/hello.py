import os
import logging
from flask import Blueprint, request, jsonify

TestController = Blueprint('hello', __name__)


@TestController.route('/hello-world', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello World!'}), 200
