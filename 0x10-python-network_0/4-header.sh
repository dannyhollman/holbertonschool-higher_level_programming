#!/bin/bash
# sends get request to URL and displays body of response
curl -sX "GET" "$@" -H "X-HolbertonSchool-User-Id: 98"
