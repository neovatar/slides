#!/usr/bin/env python3
import os
import subprocess
import time

pid = os.fork()
if pid == 0:  # child
  pid2 = os.fork()
  pid3 = os.fork()
  pid4 = os.fork()
else:
  time.sleep(2)
  os.waitpid(pid, 0)
  subprocess.check_call(('ps', 'xawuf'))
  time.sleep(60)