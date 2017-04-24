import os
import time
from slackclient import SlackClient

# Start Chrontab to watch for .txt files from slackbot_static
# 0,1,2,3,4,5,6,7,8,9,10 * * * * /home/w205/w205_Final_Project_Complete/slackbot/chronjob.sh >/dev/null

# starterbot's ID as an environment variable
BOT_ID = os.getenv("BOT_ID", "")

# constants
AT_BOT = "<@" + BOT_ID + ">"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.getenv('SLACK_BOT_TOKEN', ""))

#counter as global variable
command_count=0

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """

    if command==1:
        response = "Max Rent Price?"
    elif command==2:
        response = "Min Rent Price?"
    elif command==3:
        response = "Close to Bike Parking? Yes or No"
    elif command==3:
        response = "Close to a Bike Station? Yes or No"
    elif command==4:
        response = "Density of Offstreet Parking Near your Place? High, Medium, Low (Low if you don't care)."
    elif command==5:
        response = "Density of Schools Near your Place? High, Medium, Low (Low if you don't care)."
    elif command==6:
        response = "Density of Trees Near your Place? High, Medium, Low (Low if you don't care)."
    elif command==7:
        response = "Density of SFPD Incidents Near your Place? High, Medium, Low (High if you don't care)."
    else:
        response = "That's all the questions I have for you, check back in a few minutes as I begin my search."

    slack_client.api_call("chat.postMessage", channel=channel,
                    text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API -
        This parsing function returns None unless a message is
        directed at the Bot, based on its ID, and prints to txt.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                file=open('/home/w205/w205_Final_Project_Complete/slackbot/sfhomebot.txt','a')
                file.write(output['text'].split(AT_BOT)[1].strip().lower()+"\n")
                file.close()
                global command_count
                command_count+=1
                return command_count, \
                          output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("sfhousehunter connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
