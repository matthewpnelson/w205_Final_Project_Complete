#!/bin/bash

if [ -f /home/w205/w205_Final_Project_Complete/slackbot/sfhomebot.txt ]; then
    su - w205
    cd /data/spark15/bin/
    ./spark-submit /home/w205/w205_Final_Project_Complete/evaluation1/run_evaluation.py
    sleep 10m
    #rm /home/w205/w205_Final_Project_Complete/slackbot/sfhomebot.txt
fi
