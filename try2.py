# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:41:20 2017

@author: hi
"""

import os
import sys

from bs4 import BeautifulSoup, SoupStrainer
from unipath import Path

def main():

    ROOT = Path(os.path.realpath(__file__)).ancestor(3)
    src = ROOT.child("src")
    templatedir = src.child("templates")

    for (dirpath, dirs, files) in os.walk(templatedir):
        for path in (Path(dirpath, f) for f in files):
            if path.endswith(".html"):
                for link in BeautifulSoup(path, parse_only=SoupStrainer(target="_blank")):
                    print link

if __name__ == "__main__":
    sys.exit(main())