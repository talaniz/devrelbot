class DevRelBot:
    """A bot for handling Slack events."""


    def __init__(self, slack_client, event_data, user_list):
        self.slack_client = slack_client
        self.event_data = event_data
        self.message = self.event_data["event"]
        self.user_list = user_list

    def _is_joined_message(self):
        msg_text = self.message['text']
        if self.message.get("subtype") == "channel_join" and msg_text.endswith('joined the channel'):
            return True
        else:
            return False

    def _generate_message(self, user):
        welcome = """Welcome to our community, <@%s>!\nWe're so happy to welcome you to our community!
Please take a few minutes to review some important items including:
* Community Standards: guidelines for seeking support
* Code of Conduct: helpful rules for interacting with community members
If you have any questions, don't hesitate to reach out to us at info@delightfuldevrel.com!
Best Regards,
The Delightful DevRel Team""" % user

        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    welcome
                ),
            },
        }

    def _is_new_user(self, user):
        if user not in self.user_list:
            return True
        else:
            return False

    def send_message(self):
        welcome_title = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "Welcome to Delightful DevRel!"
                ),
            },
        }

        user = self.message["user"]
        channel = self.slack_client.conversations_open(users=[user])[
            "channel"]["id"]

        if self._is_joined_message() is True and self._is_new_user(user) is True:
            welcome_message = self._generate_message(user)
            welcome_payload = {
                "channel": channel,
                "blocks": [
                    welcome_title,
                    welcome_message,
                ],
            }
            self.slack_client.chat_postMessage(**welcome_payload)
            return user
