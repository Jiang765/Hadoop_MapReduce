#!/usr/bin/env python

import sys

valid_set = {'0', '1', '4', '5', '9'}

for line in sys.stdin:
    line = line.strip()
    temperature = line[87:92]
    quality = line[92]
    if temperature != '9999' and quality in valid_set:
        print('%s\t%d' % (line[15:23], temperature))
