#!/bin/bash

python3 generate_addon.py
docker build . -t shadow_inspector
docker run --rm -it -p 8080:8080 -v `pwd`/out:/out -v `pwd`/cert:/cert shadow_inspector