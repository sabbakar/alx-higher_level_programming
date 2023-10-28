#!/usr/bin/env bash
getResponse() {
	local url="$1"

	local responseSize
	responseSize=$(curl -s "$url" | awk '/Content-Length/ {print $2}' | tr -d '\r')
	echo "$responseSize"
}
