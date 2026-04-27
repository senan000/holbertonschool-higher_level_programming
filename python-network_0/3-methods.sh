#!/bin/bash
# This script checks a URL and lists the HTTP methods it supports.
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
