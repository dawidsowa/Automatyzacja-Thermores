from sys import argv
import pandas as pd
from airium import Airium


br = "<br/>\n"


def _a(name, href):
    return f'<a href="{href}">{name}<a/>'


class Przedmiot(Airium):
    def __init__(self, name):
        super().__init__()

        self.xlsx = pd.ExcelFile("dydaktyka/przedmioty.xlsx")
        self.dr = pd.read_excel(self.xlsx, index_col="Przedmiot").loc[name]

    def generate_literature(self, name=None):
        if not name:
            name = self.name

        self.h3(_t="Literatura podstawowa")
        with self.p():
            for r in self.dr["Literatura podstawowa"].splitlines():
                self(r)
                self.br()

        self.h3(_t="Literatura uzupełniająca")
        with self.p():
            for r in self.dr["Literatura uzupełniająca"].splitlines():
                self(r)
                self.br()

    def generate_table(
        self,
        title=None,
        name=None,
    ):
        if not name:
            name = self.name

        df = pd.read_excel(self.xlsx, sheet_name=name)
        # df.style.set_properties(**{"text-align": "left"})
        df = df.fillna("")

        for c in df.columns:
            if "-Link" in c:
                n = c.replace("-Link", "")
                df[n] = [_a(x, y) if y != "" else "" for x, y in zip(df[n], df[c])]
                df = df.drop(columns=c)

        df = df.replace({"\n": " "}, regex=True)

        if title:
            self.h3(_t=title)

        self(df.to_html(escape=False, index=False, border=False, justify="left"))

    def write(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


def generate_link(href, title):
    if not href:
        title = href

    print(a(title, href))


# generate_table("Termodynamika", )


# generate_literature("Podstawy termodynamiki")

# print(a)

# if __name__ == "__main__":
#     try:
#         title = argv[3]
#     except IndexError:
#         title = None

#     match argv[1]:
#         case "table":
#             generate_table(argv[2], title)
#         case "link":
#             generate_link(argv[2], title)
