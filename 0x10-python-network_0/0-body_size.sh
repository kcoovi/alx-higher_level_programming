#!/bin/bash
#A bash script that takes in a URL, sends request
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
