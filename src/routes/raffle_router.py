from flask import jsonify, Blueprint, request, abort
from src.models import Raffle, raffle_database

raffle_router = Blueprint('raffle_router', __name__, url_prefix='/raffles')
