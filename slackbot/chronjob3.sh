#!/bin/sh
# Set up PATH variables for SPARK
export SPARK=/data/spark15
export SPARK_HOME=$SPARK
export PATH=$SPARK/bin:$PATH

if [ -f /home/w205/w205_Final_Project_Complete/slackbot/sfhomebot.txt ]; then
    cd /data/spark15/ &&
    spark-submit /home/w205/w205_Final_Project_Complete/evaluation1/run_evaluation.py
fi
