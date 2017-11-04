#!/bin/bash

curl -X POST \
    http://127.0.0.1:8000/brapi/v1/germplasm-search \
    -H 'cache-control: no-cache' \
    -H 'content-type: application/json' \
    -H 'postman-token: 87501194-ea27-255e-160c-45f660470347' \
    -d '{
        "germplasmGenus": ["Ipomoea"]
    }'
