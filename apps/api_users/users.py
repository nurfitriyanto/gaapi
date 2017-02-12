#! apps/api_users/users.py

import traceback, sys
from flask import jsonify
from flask_restful import Resource, url_for, request
from service import manager
from utils import msg_error

class UsersRes(Resource):
    def get (self):
        try:
            output = {}
            smanager = manager()
            # Get a list of all Google Analytics accounts for the authorized user.
            accounts = smanager.management().accounts().list().execute()
            if accounts.get('items'):
                output['accounts'] = []
                output['properties'] = []
                output['profiles'] = []
                for value in accounts.get('items'):
                    xAccounts = value
                    # Get Google Analytics account id.
                    accountID = value.get('id')
                    # Get a list of all the properties
                    properties = smanager.management().webproperties().list(accountId=accountID).execute()
                    if properties.get('items'):
                        for val in properties.get('items'):
                            xProperties = val
                            # Get property id.
                            propertyID = val.get('id')
                            # Get a list of all views (profiles)
                            profiles = smanager.management().profiles().list(accountId=accountID, webPropertyId=propertyID).execute()
                            if profiles.get('items'):
                                for profile in profiles.get('items'):
                                    xProfile = profile
                    
                    output['accounts'].append(xAccounts)            
                    output['properties'].append(xProperties)
                    output['profiles'].append(xProfile)
                return jsonify(output)
            else:
                return msg_error(404, 'User Not Found')
        except Exception as e:
            print(e)
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            return msg_error(500, 'Error API')
       
