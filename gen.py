from sys import argv
import pandas as pd

xlsx = pd.ExcelFile("przedmioty.xlsx")

# df = pd.read_excel(xlsx)


br = "<br/>\n"

h3 = lambda x: f"<h3>{x}</h3>"
p = lambda x: "<p>\n" + x.replace("\n", br) + "\n</p>"


def a(name, href):
    return f'<a href="{href}">{name}<a/>'


def generate(t):
    print(
        h3("Literatura podstawowa"),
        p(t["Literatura podstawowa"]),
        h3("Literatura uzupełniająca"),
        p(t["Literatura uzupełniająca"]),
        sep="\n",
    )


def generate_table(name: str, title: str):
    df = pd.read_excel(xlsx, sheet_name=name)
    df.style.set_properties(**{"text-align": "left"})
    df = df.fillna("")

    for c in df.columns:
        if "-Link" in c:
            href = df[c]
            n = c.replace("-Link", "")
            df[n] = [a(x, y) if y != "" else "" for x, y in zip(df[n], df[c])]
            df = df.drop(columns=c)

    df = df.replace({"\n": " "}, regex=True)

    if title:
        print(h3(title))
    print(df.to_html(escape=False, index=False, border=False))


def generate_link(href, title):
    if not href:
        title = href

    print(a(title, href))


if __name__ == "__main__":
    try:
        title = argv[3]
    except IndexError:
        title = None

    match argv[1]:
        case "table":
            generate_table(argv[2], title)
        case "link":
            generate_link(argv[2], title)
