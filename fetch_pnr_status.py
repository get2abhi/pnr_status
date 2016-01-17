#!/usr/bin/python

import sys
from pnr_status import pnr_status

if len(sys.argv) != 2:
  print '\nusage --\npython pnr_status.py <PNR no.>\n'
  sys.exit(2)
  
result = pnr_status().get_pnr_status(sys.argv[1])
print result

