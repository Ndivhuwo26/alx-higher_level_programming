#!/bin/bash
#this a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sH "X-School-User-Id: 98" "$1"
echo "" 
