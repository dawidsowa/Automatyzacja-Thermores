from pathlib import Path
import pandas as pd
import numpy as np
from json import dump

pracownicy = {}
df = pd.read_excel("pracownicy/pracownicy.xlsx")
df = df.replace({np.nan: None})
for x in df.iloc:
    if x["E-mail"]:
        index = x["E-mail"].split("@")[0].replace(".", "_")
        pracownicy[index] = {
            "email": x["E-mail"],
            "name": x["Imię"],
            "tel": x["Telefon"],
            "photo": "/files/upload/157/" + x["Zdjęcie"] if x["Zdjęcie"] else None,
        }

if __name__ == "__main__":
    dump(pracownicy, Path("pracownicy.json").open("w"))
