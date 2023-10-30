#!/bin/bash
# Script to post a JSON content to a server
curl -s -H "Content-Type: application/json"  -d "$(cat "$2")" "$1"
