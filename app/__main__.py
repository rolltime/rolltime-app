# #!/usr/bin/python
# # -*- coding: utf-8 -*-

import sys
import run_scheduler
from termcolor import colored as color

#
# Run the scheduler.
#
if __name__ == '__main__':

  print '--------------------------'
  print '|    %s    |' % color("ROLLTIME COLLECT", "blue", attrs=['bold'])
  print '|       [ %s ]      |' % color("v.0.1.0", "yellow", attrs=['bold'])
  print '--------------------------'

  run_scheduler.RunScheduler()
