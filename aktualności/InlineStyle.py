#!/usr/bin/env python

import argparse
from pathlib import Path
import css_inline


def InlineStyle(html_file: Path, css_file: Path):
    html = html_file.read_text()
    css = css_file.read_text()
    joined = f"<style>\n{css}\n</style>\n{html}"

    inlined = css_inline.inline(joined)
    print(joined)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="InlineStyle")
    parser.add_argument("html_file", metavar="html_file", type=Path, help="file name")
    parser.add_argument("css_file", metavar="css_file", type=Path, help="file name")
    parser.add_argument("css_file", metavar="css_file", type=Path, help="file name")
    args = parser.parse_args()

    InlineStyle(args.html_file, args.css_file)
