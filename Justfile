pull:
    #!/usr/bin/env nu
    # rclone backend copyid google-pwr: 1zz1s2fZ-mcynESq3NeJ0z23Tl_sshgKjNL3phbsX7UE .import/pracownicy.xlsx
    def "update --skip-missing" [path: cell-path f:any] {
      each {|r| if (($r | get --ignore-errors $path) == null) {$r} else {$r | update $path $f}}
    }
    
    open --raw .import/pracownicy.xlsx
      | from xlsx  --sheets ["Doktoranci"]
      | get Doktoranci
      | headers
      | reject Zmiana Content 
      | rename --block {str downcase | str replace --all " " "_"}
      | update --skip-missing e-mail {$in|str replace "@pwr.edu.pl" ""}
      | rename --column {"imię": name, e-mail: id, telefon: tel,słowa_kluczowe: keywords, obszar_badań: text, "zdjęcie": photo}
      | update --skip-missing keywords {$in | split row --regex  '\s*,\s*' | str trim}
      | to json
      | save -f ".import/doktoranci.json"

  
run:
  #!/usr/bin/env nu
  cd clojure
  ./parse.nu