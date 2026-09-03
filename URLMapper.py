#!/usr/bin/env python
"""urlmapper.py"""

# Jordan Ranji - CSCI 5253

import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        # Check if it starts with href=", then take everything inside the quotation marks if it does
        # really simple url check, no http check or URL library used
        if len(word) > 6:
            if word[:6] == "href=\"":
                cur_word = word[6:]
                # find next quotation mark
                quote_index = cur_word.find("\"")
                url = cur_word[:quote_index] # keep everything before the last quotation mark
                print('%s\t%s' % (url, 1))
