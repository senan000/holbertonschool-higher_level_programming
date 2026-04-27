#!/bin/bash
# This script requests a URL with a custom header (User-Id: 98) and shows the response body.
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
