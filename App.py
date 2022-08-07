import logging
import os
from dotenv import load_dotenv
from slack_bolt import App, app
from slack_bolt.adapter.socket_mode import SocketModeHandler
from chatbot import AlexBot

logging.basicConfig(level=logging.INFO)

load_dotenv()

SLACK_BOT_TOKEN = os.environ["ACA_Example_App_Bot_User_OAuth_Token"]
SLACK_APP_TOKEN = os.environ["ACA_Example_App_Socket_Mode_Token"]

app = App(token=SLACK_BOT_TOKEN)

alex_bot = AlexBot()


@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    say("Hey! What can I do for you?")


@app.event("message")
def message_handler(body, context, payload, options, say, event):
    text = event.get('text')
    say(alex_bot.answer_anything(text))


@app.event("team_join")
def ask_for_introduction(event, say):
    welcome_channel_id = "C12345"
    user_id = event["user"]
    text = f"Welcome to the team, <@{user_id}>! 🎉 You can introduce yourself in this channel."
    say(text=text, channel=welcome_channel_id)


@app.command("/hello-bolt-python")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
