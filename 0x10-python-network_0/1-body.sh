#!/bin/bash
# Sends a GET request to a URL and displays the body of the response
curl -s "$1" -X GET -d "" -L
