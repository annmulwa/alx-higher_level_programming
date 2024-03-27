#!/bin/bash
# Display only body of a 200 status code response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && curl -s "$1"
