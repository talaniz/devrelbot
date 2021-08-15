import os
import sqlite3
from urllib.parse import parse_qs

from dotenv import load_dotenv
from flask import Flask, request
from slack import WebClient
from slack.errors import SlackApiError

from slackeventsapi import SlackEventAdapter

load_dotenv()

app = Flask(__name__)
slack_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
slack_events_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], endpoint="/slack/events", server=app)
        
    
# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    # Also need to account for when a bot posts a message (error = "cannot_dm_bot")
    # this is a code smell and requires some functions to make it more readable
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        user = message["user"]
        message = "Hello <@%s>! :tada:" % message["user"]
        # post in the channel
        # slack_client.chat_postMessage(channel=channel, text=message)
        # send a direct message to the user
        im = slack_client.conversations_open(users=[user])
        slack_client.chat_postMessage(channel=im["channel"]["id"], text=message)

@app.route("/")
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run(port=5000)
