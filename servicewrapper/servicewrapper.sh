#!/usr/bin/env bash
export CONTAINERIP=$(hostname  -I | cut -f1 -d' ')

curl -X POST http://consul.service.consul:8500/v1/agent/service/register \
  --header 'Content-Type: application/json' \
  --data-binary '{"ID": "'"helloworld-$HOSTNAME"'", "Name": "helloworld", "Address": "'"$CONTAINERIP"'", "Port": 80, "Check": {"HTTP": "http://'"$CONTAINERIP"'", "Interval": "30s"}}'
