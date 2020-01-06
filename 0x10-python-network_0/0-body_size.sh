#!/usr/bin/env bash
# send request to url and display body size of response

curl -s "$1" | wc -c
