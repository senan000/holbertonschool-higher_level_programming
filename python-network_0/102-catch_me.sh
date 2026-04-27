#!/bin/bash
# This script requests a specific URL and shows a response containing 'You got me!'.
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
