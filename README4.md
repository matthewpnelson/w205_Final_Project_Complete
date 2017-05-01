# w205_Final_Project_Complete
Berkeley MIDS w205 Final Project - SF Housing Slackbot


To Run Slackbot:

###### ENVIRONMENT SETUP IN ROOT #########
###### SLOW BECAUSE VERSION SWITCH-OUTS########

# Launch an instance of UCB W205 Spring 2016 & attach an EBS volume

# Attach class /data folder
mount -t ext4 /dev/xvdf /data
chmod a+rwx /data

# Setup Systems
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh

#./setup_ucb_complete_plus_postgres.sh <*the device path to EBS volume*>
./setup_ucb_complete_plus_postgres.sh /dev/xvdf

# Clone Github repo to /data
git clone https://github.com/matthewpnelson/w205_Final_Project_Complete.git

# Run Init Script
cd w205_Final_Project_Complete/initialize/
chmod +x initialize3.sh
./initialize3.sh
# Answer prompt to download Y for fixing certificate issues

######### ENVIRONMENT SETUP SWITCHES YOU TO USER W205##########

exit
cd

#SSL and certificate setup for Python 2.7
sudo yum install gcc libffi-devel python-devel openssl-devel
pip install cryptography
pip install urllib3[secure]
# Answer prompt to download Y for fixing certificate issues

su - w205

# Clone Github repo to user /w205
git clone https://github.com/matthewpnelson/w205_Final_Project_Complete.git

# Set up PATH variables for SPARK
export SPARK=/data/spark15
export SPARK_HOME=$SPARK
export PATH=$SPARK/bin:$PATH

##### 
# Start Scraper
# Run start_scraper Script to begin active scraping (Pulls 50 entries from Craigslist every 20 mins) & saves to Hive
cd /home/w205/w205_Final_Project_Complete/scraper/
chmod +x start_scraper.sh
./start_scraper.sh
### THE SCRAPING IS NOW RUN - DO NOT CLOSE SESSION ###

######OPEN A NEW SESSION#####
# python -- version should be Python 2.7
cd w205_Final_Project_Complete/initialize
chmod +x spark_setup.sh
./spark_setup.sh
export SPARK=/data/spark15
export SPARK_HOME=$SPARK
export PATH=$SPARK/bin:$PATH

cd
/data/start_metastore.sh
enter


#### SWITCH USERS#### 

su - w205
cd w205_Final_Project_Complete/slackbot

### Make cronjob ###
crontab -e
press 'o' to edit
insert: * * * * * /home/w205/w205_Final_Project_Complete/slackbot/chronjob3.sh
press esc
:wq

### Start Slackbot ###
chmod +x chronjob3.sh
# Set Slack Tokens as Environment Variables 
export SLACK_TOKEN=' ' 
export BOT_ID=' ' 
export SLACK_BOT_TOKEN=' '
python sfhomebot.py

#####
# Submit Queries to Slackbot via Slack Channel



