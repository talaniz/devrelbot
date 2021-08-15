import os

from dotenv import load_dotenv
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from devrelbot import DevRelBot

load_dotenv()

app = Flask(__name__)
slack_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
slack_events_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], endpoint="/slack/events", server=app)
user_list = []

slack_client.users_info
@slack_events_adapter.on("message")
def handle_message(event_data):
    devrelbot = DevRelBot(slack_client, event_data, user_list)

    user = devrelbot.send_message()
    user_list.append(user)

@app.route("/")
def index():
    if len(user_list) > 0:
        return ' '.join(e for e in user_list)
    else:
        return "no new users"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)