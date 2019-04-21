import os
from flask import current_app
from slackclient import SlackClient

def send_trumpet(text):
    slack_client = SlackClient(current_app.config['SLACK_BOT_TOKEN'])
    channel = current_app.config['SLACK_BOT_CHANNEL']
    username = current_app.config['SLACK_BOT_USERNAME']

    slack_client.api_call("chat.postMessage", channel=channel, text=text, username=username)

