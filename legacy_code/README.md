# w205_Final_Project_Complete
Berkeley MIDS w205 Final Project - SF Housing Slackbot


To Run Slackbot:

##### 
# Launch an instance of UCB W205 Spring 2016 ami-be0d5fd4 & attach an EBS volume
Use Hadoop Cluster UCB Security Settings
4040, 50070, 8080, 22, 7180, 8088 all open to 0.0.0.0/0

# Build /data folder
fdisk -l <use this location below)

cd 
mkdir /data
chmod a+rwx /data

# Setup Systems
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh

#./setup_ucb_complete_plus_postgres.sh <*the device path to EBS volume*>
./setup_ucb_complete_plus_postgres.sh /dev/xvdb


##### 
# Clone Github repo to /data as w205 user
su - w205
git clone https://github.com/matthewpnelson/w205_Final_Project_Complete.git
exit

##### 
# Run Init Script
cd /home/w205/w205_Final_Project_Complete/initialize/
chmod +x initialize.sh
./initialize.sh


##### 
# Start Scraper
# Run start_scraper Script to begin active scraping (Pulls 50 entries from Craigslist every 20 mins) & saves to Hive
###########################################
cd /home/w205/w205_Final_Project_Complete/scraper/
chmod +x start_scraper.sh
./start_scraper.sh
###########################################

#####
# Set Slack Tokens as Environment Variables 
export SLACK_TOKEN=' ' 
 


#####
# Set Slackbot Tokens as Env Variables
export SLACK_BOT_TOKEN=' '
python print_bot_id.py
# copy bot id and set ENV variable
export BOT_ID=' ' 

# Start Slackbot

#crontab -e
# add in * * * * * 
crontab -r
##########################################
chmod +x /home/w205/w205_Final_Project_Complete/slackbot/chronjob.sh
cd /home/w205/w205_Final_Project_Complete/slackbot/
export BOT_ID='U53U07EVC'
export SLACK_BOT_TOKEN='xoxb-173952252998-hbSa4LuG31wytVTYQkhlttAa'
export SLACK_TOKEN='xoxp-160110468034-173023780387-173896965970-b9e8cead22e2e23f7fac439ea7f72c05' 
python sfhomebot.py
###########################################

crontab chrontab.txt

#To Manually Run Filtering Script
###########################################
cd /data/spark15/bin
./spark-submit /home/w205/w205_Final_Project_Complete/evaluation1/run_evaluation.py
###########################################

#####
# Submit Queries to Slackbot via Slack Channel

#####
# When Done
Shut down Slackbot & 
crontab -r

