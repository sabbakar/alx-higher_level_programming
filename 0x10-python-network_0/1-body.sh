#!/bin/bash
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
[ "$response" -eq 200 ] && curl -s "$1"
