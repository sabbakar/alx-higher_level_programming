#!/bin/bash
# Script to post a JSON content to a server
curl -X POST -H "Content-Type: application/json" --data "my_json_0" "$1"
