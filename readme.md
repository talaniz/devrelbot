# DevRelBot

DevRelBot is a project that demonstrates Slackbot functionality to show the value of automation in managing communities.

# Project Setup

Project setup consists of creating a Slack bot and setting up a local environment for testing.

## Local development
* Create a new Slack application in the [Slack API Control Panel](https://api.slack.com/apps) (see [Creating the Slackbot in the Slack UI](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04)) and install it in you workspace.
* Create a `.env` file, define `SLACK_BOT_TOKEN` and `SLACK_BOT_TOKEN` from the previous step.
* Install [ngrok](https://ngrok.com/) for localhost tunneling.
* Clone this project locally.
* Create a virtualenv, `python3 -m venv /path/to/env`.
* Install pre-requisites, `cd env && pip -r install requirements.txt`.
  
## Running the project
* In a terminal window, run `ngrok http 5000`.
* Take the resulting domain name and add it as the Request URL in [Event Subscriptions](https://api.slack.com/apps/A015T8ETJ92/event-subscriptions?) (ex. - `https://597dd46b15c8.ngrok.io/slack/events`).
* Change into the project directory and run `flask run`.
* Join a channel to see the bot send a direct welcome message.