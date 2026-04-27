#!/bin/bash
#This script gets a URL and shows the size of its response body.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
