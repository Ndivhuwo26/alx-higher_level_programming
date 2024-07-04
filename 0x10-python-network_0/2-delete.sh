#!/bin/bash
# Bash script that sends a DELETE request to the URL passed

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -X DELETE "$1")


if [ $? -ne 0 ]; then
    echo "Error: Failed to execute curl command"
    exit 1
fi

echo "$response"
