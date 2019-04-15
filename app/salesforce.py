from app import app
from flask import jsonify
import requests
from simple_salesforce import Salesforce

def authenticate():
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

    return ({"access_token": access_token, "instance_url": instance_url})

def unsubscribe_user(email):
    auth = authenticate()

    sf = Salesforce(instance=auth['instance_url'], session_id=auth['access_token'])
    contact_query = "SELECT Id, HasOptedOutOfEmail FROM Contact WHERE email = '" + email + "'"
    contact_records = sf.query(contact_query)

    if contact_records["totalSize"] == 0:
        response = {"status_code": 500}
        return(response)
    else:
        previously = False
        for contact in contact_records["records"]:
            if(contact['HasOptedOutOfEmail'] == True):
                previously = True
            sf.Contact.update(contact["Id"],{'HasOptedOutOfEmail':'true'})
        response = {"status_code": 200, "previously": previously}
    return(response)
