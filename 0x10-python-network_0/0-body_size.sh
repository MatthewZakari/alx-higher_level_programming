#!/bin/bash
# Sends a request to a URL and displays response size in bytes
curl -s "$1" | grep -i Content-Length | awk '{print $2}
