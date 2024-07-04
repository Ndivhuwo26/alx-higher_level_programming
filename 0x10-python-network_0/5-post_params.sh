#!/bin/bash
#this  a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
echo ""

