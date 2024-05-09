#!/bin/bash
# Sends a POST request with specified parameters to a given URL and displays the response body

curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"

