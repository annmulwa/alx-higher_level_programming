#!/bin/bash
# Display only body of a 200 status code response
response=$(curl -s -o /tmp/response.txt -w "%{http_code}" "$1" && cat /tmp/response.txt | awk 'NR > 1') && [ "$response" -eq 200 ] && cat /tmp/response.txt
