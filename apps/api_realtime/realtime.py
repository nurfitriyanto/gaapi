#! appps/api_reltime/realtime.py

import traceback, sys
from flask import jsonify
from flask_restful import Resource, url_for, request
from service import manager
from utils import msg_error

class RealtimeRes(Resource):
    def get (self):
        try:
            smanager = manager()
            profileId = request.args.get('profileId')
            # Use the Analytics Service Object to query the Core Realtime API
            output = smanager.data().realtime().get(
                ids='ga:' + profileId,
                metrics='rt:activeUsers',
                dimensions='rt:userType,rt:browser, rt:operatingSystem, rt:deviceCategory, rt:country'
            ).execute()
                
            return jsonify(output)
        except Exception as e:
            print(e)
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            return msg_error(500, 'Error API')

        
