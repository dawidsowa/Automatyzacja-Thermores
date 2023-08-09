#!/usr/bin/env python

import argparse

def ${TM_FILENAME_BASE}():
    pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="${TM_FILENAME_BASE}")
    parser.add_argument("file", metavar="file", type=str, nargs=1, help="file name")
    args = parser.parse_args()

    ${TM_FILENAME_BASE}()
