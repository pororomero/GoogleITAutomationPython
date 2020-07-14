#!/usr/bin/env python3

import os

# get method allow us to return custom data if not present key is provided


print("HOME: {}".format(os.environ.get("HOME", "")))
print("SHELL: {}".format(os.environ.get("SHELL", "")))
print("FRUIT: {}".format(os.environ.get("FRUIT", "")))  


