#! /bin/bash

cd

# Start Hadoop
./start_hadoop.sh
/data/start_postgres.sh

#start Hive Metastore
/data/start_metastore.sh

# Set up Spark
cd /home/w205/w205_Final_Project_Complete/initialize/
chmod +x spark_setup.sh
./spark_setup.sh

# Set up PATH variables for SPARK
export SPARK=/data/spark15
export SPARK_HOME=$SPARK
export PATH=$SPARK/bin:$PATH

#start Hive Metastore
/data/start_metastore.sh



## Install and set up Python 2.7 and PIP 2.7 (needed for SlackClient)
# install build tools
sudo yum install make automake gcc gcc-c++ kernel-devel git-core -y
# install python 2.7 and change default python symlink
sudo yum install python27-devel -y
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python2.7 /usr/bin/python
# yum still needs 2.6, so write it in and backup script
sudo cp /usr/bin/yum /usr/bin/_yum_before_27
sudo sed -i s/python/python2.6/g /usr/bin/yum
sudo sed -i s/python2.6/python2.6/g /usr/bin/yum
# should display now 2.7.5 or later:
python -V
# now install pip for 2.7
sudo curl -o /tmp/ez_setup.py https://bootstrap.pypa.io/ez_setup.py
sudo /usr/bin/python2.7 /tmp/ez_setup.py
#sudo /usr/bin/easy_install-2.7 pip

wget --no-check-certificate http://pypi.python.org/packages/source/d/distribute/distribute-0.6.35.tar.gz
tar xf distribute-0.6.35.tar.gz
cd distribute-0.6.35
python2.7 setup.py install
easy_install-2.7 pip
sudo pip install virtualenv
# should display current versions:
pip -V && virtualenv --version
#SSL and certificate setup before updating Python
sudo yum install gcc libffi-devel python-devel openssl-devel
pip install cryptography
pip install urllib3[secure]


# Manually Install Craigslist Scraper as root user
pip install python-craigslist --upgrade

# Manually Install Slackclient as root user
pip install slackclient



# download all static data, load data lake
cd /home/w205/w205_Final_Project_Complete/initialize/
chmod +x slackbot_load_data_lake.sh
# change to w205 user
su - w205
./home/w205/w205_Final_Project_Complete/initialize/slackbot_load_data_lake.sh
exit

# Run Hive DDL Statements to build static data tables
chmod +x /home/w205/w205_Final_Project_Complete/initialize/slackbot_hive_base_ddl.sql
hive -f /home/w205/w205_Final_Project_Complete/initialize/slackbot_hive_base_ddl.sql

# Run Spark to see if the Hive tables are there & Spark is synced up
##./data/spark15/bin/spark-sql

# run ranking scripts on some Hive Tables in Spark-SQL NOT FINISHED
#cd /data/spark15/bin/
