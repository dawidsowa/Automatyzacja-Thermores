import pandas as pd


def _a(name, href):
    return f'<a href="{href}">{name}<a/>'


def generate(xlsx, name):
    df = pd.read_excel(xlsx, sheet_name=name)
    # df.style.set_properties(**{"text-align": "left"})
    df = df.fillna("")

    for c in df.columns:
        if "-Link" in c:
            n = c.replace("-Link", "")
            df[n] = [_a(x, y) if y != "" else "" for x, y in zip(df[n], df[c])]
            df = df.drop(columns=c)

    df = df.replace({"\n": " "}, regex=True)

    print(df.to_html(escape=False, index=False, border=False, justify="left"))
