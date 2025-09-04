#!/usr/bin/env python3
import sys
import re

url_pattern = re.compile(r'https?://[^\s,")]+')

for line in sys.stdin:
    urls = url_pattern.findall(line)
    for url in urls:
        print(f"{url}\t1")