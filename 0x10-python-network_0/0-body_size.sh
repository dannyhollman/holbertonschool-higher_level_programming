#!/usr/bin/bash
# send request to url and display body size of response
curl -s "$@" | wc -c
