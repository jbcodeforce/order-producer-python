#!/bin/bash


fname=$PWD/data/order1.json
hostn=order-producer-python-reefer-shipment-solution.greencluster-fa9ee67c9ab6a7791435450358e564cc-0001.us-east.containers.appdomain.cloud

url="http://$hostn/order"

echo ""
echo "Send $fname to $url"
curl -v  -H "accept: */*" -H "Content-Type: application/json" -d @$fname $url
curl 