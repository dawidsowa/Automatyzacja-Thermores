#!/usr/bin/env python

import argparse
from pathlib import Path
from subprocess import run
import css_inline


# Przykład:
# ./InlineStyle.py dofinansowanie.md ../styles/style.css dofinansowanie.html -fmarkdown-implicit_figures


def InlineStyle(
    input_file: Path, css_file: Path, output_file: Path | None, pandoc_args
):
    if input_file.suffix == ".md":
        html = run(
            ["pandoc", input_file, *pandoc_args], capture_output=True, text=True
        ).stdout
    else:
        html = input_file.read_text()
    css = css_file.read_text()
    joined = f"<style>\n{css}\n</style>\n{html}"

    inliner = css_inline.CSSInliner(extra_css=css)
    inlined = inliner.inline(joined)
    if not "--standalone" in pandoc_args:
        inlined = inlined.replace(
            """<html><head>
</head><body>""",
            "",
        ).replace("</body></html>", "")

    if output_file:
        output_file.write_text(inlined)
    else:
        print(inlined)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="InlineStyle", description="Dodaje CSS do pliku html lub markdown"
    )
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
    parser.add_argument(
        "pandoc_args",
        nargs=argparse.REMAINDER,
        help="Wszystkie inne argumenty zostaną przekazane do pandoc",
    )
    args = parser.parse_args()

    InlineStyle(args.input_file, args.css_file, args.output_file, args.pandoc_args)
