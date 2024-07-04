#!/bin/bash
#a Bash script that will  takes in a URL and displays all HTTP methods the server will accept.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

allowed_methods=$(curl -sI "$1" | grep "Allow" | cut -d " " -f 2-)


if [ -z "$allowed_methods" ]; then
    echo "Error: Server did not provide Allow header for HTTP methods"
    exit 1
fi


echo "$allowed_methods"
