#!/bin/bash
# To retrieve status code
curl -s -o /dev/null -w "%{http_code}" your_url_here
