#! apps/routes.py

from flask import Blueprint
from flask_restful import Api, Resource, url_for
from apps.api_report.report import ReportRes
from apps.api_users.users import UsersRes

apis = Blueprint('apis', __name__, url_prefix='/api/v1')

api = Api(apis)
api.add_resource(ReportRes, '/report')
api.add_resource(UsersRes, '/user')
