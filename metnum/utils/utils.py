import sys
import os

def debug_print(msg, debug):
    if debug:
        sys.stdout.write(msg + "\n")
