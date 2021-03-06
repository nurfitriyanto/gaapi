#! appps/api_report/report.py

import traceback, sys
from flask import jsonify
from flask_restful import Resource, url_for, request
from service import manager
from utils import msg_error

class ReportRes(Resource):
    def get (self):
        try:
            smanager = manager()
            profileId = request.args.get('profileId')
            # Use the Analytics Service Object to query the Core Reporting API
            # for the number of sessions in the past seven days.
            output = smanager.data().ga().get(
                ids='ga:' + profileId,
                start_date='7daysAgo',
                end_date='today',
                metrics='ga:sessions'
            ).execute()
                
            return jsonify(output)
        except Exception as e:
            print(e)
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            return msg_error(500, 'Error API')

        
