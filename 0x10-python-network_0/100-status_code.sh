#!/bin/bash
# displays the status code of the reponse
curl -s -o /dev/null -w "%{http_code}" "$@"
