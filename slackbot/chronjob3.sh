#!/bin/sh

if [ -f /home/w205/w205_Final_Project_Complete/slackbot/sfhomebot.txt ]; then
    spark-submit /home/w205/w205_Final_Project_Complete/evaluation1/run_evaluation.py
fi
