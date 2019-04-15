from app import app
from flask import jsonify
import requests
from simple_salesforce import Salesforce

def unsubscribe_user(email):
    params = {
        "grant_type": "password",
        "client_id": app.config['CONSUMER_KEY'],
        "client_secret": app.config['CONSUMER_SECRET'],
        "username": app.config['SF_USERNAME'],
        "password": app.config['SF_PASSWORD'] + app.config['SF_SECURITY_TOKEN']
    }

    r = requests.post(app.config['SF_OAUTH'], params=params)

    access_token = r.json().get("access_token")
    instance_url = app.config['SF_INSTANCE_URL']

    sf = Salesforce(instance=instance_url, session_id=access_token)
    contact_query = "SELECT Id FROM Contact WHERE email = '" + email + "'"
    contact_records = sf.query(contact_query)

    if contact_records["totalSize"] == 0:
        response = {"status_code": 500, "text": "Record not found"}
    else:
        for contact in contact_records["records"]:
            contact_id = contact["Id"]
            sf.Contact.update(contact_id,{'HasOptedOutOfEmail':'true'})
        response = {"status_code": 200, "text": "Success"}
    return jsonify(response)
