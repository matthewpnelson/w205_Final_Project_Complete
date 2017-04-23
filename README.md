# w205_Final_Project_Complete
Berkeley MIDS w205 Final Project - SF Housing Slackbot


To Run Slackbot:

##### 
# Launch an instance of UCB W205 Spring 2016 & attach an EBS volume

# Build /data folder
cd 
mkdir /data
chmod a+rwx /data

# Setup Systems
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh

#./setup_ucb_complete_plus_postgres.sh <*the device path to EBS volume*>
./setup_ucb_complete_plus_postgres.sh /dev/xvdb


##### 
# Clone Github repo to /data
cd /home/w205
git clone https://github.com/matthewpnelson/w205_Final_Project_Complete.git


##### 
# Run Init Script
cd /home/w205/w205_Final_Project_Complete/initialize/
chmod +x initialize.sh
./initialize.sh


##### 
# Start Scraper
# Run start_scraper Script to begin active scraping (Pulls 50 entries from Craigslist every 20 mins) & saves to Hive
cd /home/w205/w205_Final_Project_Complete/scraper/
chmod +x start_scraper.sh
./start_scraper.sh


#####
# Set Slack Tokens as Environment Variables 
export SLACK_TOKEN=' ' 
export BOT_ID=' ' 
export SLACK_BOT_TOKEN=' ' 


#####
# Start Slackbot
chmod +x chronjob.sh
0,1,2,3,4,5,6,7,8,9,10 * * * * /home/w205/w205_Final_Project_Complete/slackbot/chronjob.sh >/dev/null
python sfhomebot.py

#####
# Submit Queries to Slackbot via Slack Channel



