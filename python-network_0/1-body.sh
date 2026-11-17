#!/bin/bash
# Sends a GET request to the URL, following redirects, and displays the body only for a 200 response
curl -s -L -o /tmp/body -w "%{http_code}" "$1" | grep -qx 200 && cat /tmp/body
