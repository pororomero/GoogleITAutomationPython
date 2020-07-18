#!/usr/bin/env python3

import os
import subprocess
# Calling this method of the os.environ dictionary will
# copy the current environment variables to store and prepare a new environment.
my_env = os.environ.copy() # contains the environment variables
# adding one additional PATH variables
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
