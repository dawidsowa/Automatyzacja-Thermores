import netrc
from subprocess import run
from json import dump, load, dumps, loads
from pathlib import Path
from sys import argv
import uuid
import numpy as np

import pandas as pd
from airium import Airium
from html import escape

# linkText=dr inż. Cezary Czajkowski


def gen():
    pracownicy = {}
    df = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/1zz1s2fZ-mcynESq3NeJ0z23Tl_sshgKjNL3phbsX7UE/export?format=csv&gid=0"
    )
    df["Content"].fillna("", inplace=True)
    df = df.replace({np.nan: None})

    for c in df.iloc:
        # print(f"<h3>{c['Stopień'] + c['Imię i nazwisko']}</h3>")
        # a.h3(_t=)
        if not c["Zmiana"]:
            continue
        if not c["Content"]:
            c["Content"] = ""
        if not c["E-mail"]:
            pracownicy[c["Imię"]] = c["Content"]
            continue

        a = Airium()
        if c["Zdjęcie"]:
            with a.figure(
                klass="profile-picture", style="float: right; max-width: 25%"
            ):
                a.img(
                    src="https://thermores.pwr.edu.pl/files/upload/157/" + c["Zdjęcie"]
                )

        with a.dl(id=c["E-mail"].split("@")[0], klass="pracownik"):
            for x in [
                "Temat pracy doktorskiej",
                "Promotor",
                "Obszar badań",
                "Słowa kluczowe",
                "Biuro",
            ]:
                if c[x]:
                    a.dt(_t=x)
                    a.dd(_t=c[x].replace("\n", "<br/>\n"))
            a.dt(_t="Telefon")
            with a.dd():
                a.a(href="tel:" + c["Telefon"], _t=c["Telefon"])
            a.dt(_t="E-mail")
            with a.dd():
                a.a(href="mailto:" + c["E-mail"], _t=c["E-mail"])

        pracownicy[c["Imię"]] = str(a) + c["Content"]

    return pracownicy


i = 0


def append_prac(nazwa, zaw, base, dic):
    auth = netrc.netrc().authenticators("thermores.pwr.edu.pl")
    global i
    test = base
    test["id"] = str(uuid.uuid1())
    test["name"] = f"{i} - {nazwa}"
    test = loads(
        dumps(test)
        .replace("${title}", dumps(nazwa)[1:-1])
        .replace("${content}", dumps(zaw)[1:-1])
        .replace("${password}", dumps(auth[2])[1:-1])
        .replace("${username}", dumps(auth[0])[1:-1])
    )
    dic["tests"].append(test)
    i += 1


def add_to_side(filename, pracownicy):
    p = Path(filename)
    dic = load(p.open(encoding="utf-8"))

    base = dic["tests"][0]
    del dic["tests"][0]

    for k, v in pracownicy.items():
        print(k)
        append_prac(nazwa=k, zaw=v, base=base, dic=dic)

    np = p.with_suffix(".new.side")

    np.write_text(dumps(dic, sort_keys=True, indent=4), newline="\n")


if __name__ == "__main__":
    add_to_side("Thermores.side", gen())
