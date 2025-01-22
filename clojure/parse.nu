#!/usr/bin/env nu

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
