#!/usr/bin/python3

import time
import upnpy
import sys
import os 

sys.stdout.write("[*]Upnp M-SEARCH Daemon started\n")

while True == True:
  upnp = upnpy.UPnP()
  sys.stdout.write("[*]Searching for Devices..\n")
  devices = upnp.discover()
  sys.stdout.write("[*]Devices Search Finsihed... \n [*]Returning list\n\n")
  print(devices)
  sys.stdout.write("[*]Waiting for next execution...\n")
  time.sleep(60)
