#!/bin/bash

url='http://35.208.97.187:8000'
token='ac072a2c5733b55af66b27a4cb8179a7f314a9c7'
pyats create testbed netbox --output testbed.yaml --netbox-url=$url --user-token=$token
genie shell --testbed-file testbed.yaml --replay mocked_devices
