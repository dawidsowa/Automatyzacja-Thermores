#!/usr/bin/env python

import argparse


def InlineStyle(html_file, css_file):
    print(html_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="InlineStyle")
    parser.add_argument(
        "html", metavar="html_file", type=str, nargs=1, help="file name"
    )
    parser.add_argument("css", metavar="css_file", type=str, nargs=1, help="file name")
    args = parser.parse_args()

    InlineStyle(args.html_file, args.css_file)
