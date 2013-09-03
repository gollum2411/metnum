import sys
import os

def debug_print(msg, debug=False):
    if debug:
        sys.stdout.write(msg + "\n")
