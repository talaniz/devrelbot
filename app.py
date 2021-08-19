import os

from dotenv import load_dotenv
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

load_dotenv()

app = Flask(__name__)
slack_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
slack_events_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], endpoint="/slack/events", server=app)
        

@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]

    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        user = message["user"]
        message = "Hello <@%s>! :tada:" % message["user"]
        im = slack_client.conversations_open(users=[user])
        slack_client.chat_postMessage(channel=im["channel"]["id"], text=message)

@app.route("/")
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run(port=5000)
