#!/usr/bin/env python

import argparse
from pathlib import Path
from subprocess import run
import css_inline


def InlineStyle(input_file: Path, css_file: Path, output_file: Path | None):
    if input_file.suffix = ".md":
        html = run(["pandoc", input_file], capture_output=True, text=True).stdout
    else:
        html = input_file.read_text()
    css = css_file.read_text()
    joined = f"<style>\n{css}\n</style>\n{html}"

    inlined = css_inline.inline(joined)

    if output_file:
        output_file.write_text(inlined)
    else:
        print(inlined)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="InlineStyle")
    parser.add_argument("input_file", metavar="input_file", type=Path, help="file name")
    parser.add_argument("css_file", metavar="css_file", type=Path, help="file name")
    parser.add_argument(
        "output_file",
        metavar="output_file",
        nargs="?",
        default=None,
        type=Path,
        help="file name",
    )
    args = parser.parse_args()

    InlineStyle(args.input_file, args.css_file, args.output_file)
