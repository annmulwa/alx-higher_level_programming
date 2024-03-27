#!/bin/bash
# Display only body of a 200 status code response
curl -s -w "%{http_code}" "$1" | awk 'NR==1 && $0 == 200 {p=1} p' | tail -n +2
