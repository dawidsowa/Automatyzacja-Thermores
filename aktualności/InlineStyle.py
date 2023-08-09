#!/usr/bin/env python

import argparse
from pathlib import Path


def InlineStyle(html_file, css_file):
    print(html_file.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="InlineStyle")
    parser.add_argument("html_file", metavar="html_file", type=Path, help="file name")
    parser.add_argument("css_file", metavar="css_file", type=str, help="file name")
    args = parser.parse_args()

    InlineStyle(args.html_file, args.css_file)
