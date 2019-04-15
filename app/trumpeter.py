from app import app
import os
from slackclient import SlackClient

def send_trumpet(text):
    slack_client = SlackClient(app.config['SLACK_BOT_TOKEN'])
    channel = app.config['SLACK_BOT_CHANNEL']
    username = app.config['SLACK_BOT_USERNAME']

    slack_client.api_call("chat.postMessage", channel=channel, text=text, username=username)

