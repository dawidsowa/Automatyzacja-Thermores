#!/usr/bin/env nu
open doktoranci.csv
    | rename --block {str downcase | str replace --all " " "_"}
    | update e-mail {$in | str replace "@pwr.edu.pl" ""}
    | rename --column {"imię": name, e-mail: id, telefon: tel,słowa_kluczowe: keywords, obszar_badań: text, "zdjęcie": photo}
    | update keywords {$in | split row --regex  '\s*,\s*' | str trim}
    | reject  zmiana
    | each {}
    | to json
    | save -f "doktoranci.json"

cat old.html | save -f new.html
clojure -M printer.clj | save --append new.html
echo '<h3>Pracownicy techniczni</h3><div class="accordion text-content">
<button class="accordion-title">
Aleksander Krzywdziński    </button>

<div class="accordion-text" style="">
<dl id="aleksander.krzywdzinski" class="pracownik">
<dt>Biuro</dt>
<dd>bud. D-2 (laboratorium)</dd>
<dt>Telefon</dt>
<dd><a href="tel:+48 (71) 320 33 46">+48 (71) 320 33 46</a></dd>
<dt>E-mail</dt>
<dd><a href="mailto:aleksander.krzywdzinski@pwr.edu.pl">aleksander.krzywdzinski@pwr.edu.pl</a></dd>
</dl>            </div>
</div>
' | save --append new.html
