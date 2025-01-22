(require '[hiccup2.core :as h]
         '[cheshire.core :as json]
         '[clojure.java.io :as io])
(require 'clojure.walk)
(use '[clojure.string :only (join blank?)])
(defn mapply [f & args] (apply f (apply concat (butlast args) (last args))))
(def doktoranci (map clojure.walk/keywordize-keys (json/parse-stream (clojure.java.io/reader "../.import/doktoranci.json"))))
(defn mailto [email] [:a
                      {:href (str "mailto:" email)}
                      email])
(defn telto [number] [:a
                      {:href (str "tel:+48 " number)}
                      (str "+48 " number)])
(defn parse [pair] (if (and (string? (last pair)) (not (blank? (last pair)))) [[:dt (first pair)] [:dd (last pair)]] nil))

(defn box [& {:keys [name id tel keywords promotor text temat_pracy_doktorskiej photo biuro]}]
  (let [pairs [["Temat pracy doktorskiej" temat_pracy_doktorskiej]
               ["Promotor" promotor]
               ["Obszar badań" text]
               ["Słowa kluczowe" (join ", " keywords)]
               ["Biuro" biuro]
               ["Telefon" (telto tel)]
               ["E-mail" (mailto (str id "@pwr.edu.pl"))]]]
    [:div
     {:class "accordion text-content"}
     [:button {:class "accordion-title"} name]
     [:div
      {:class "accordion-text"}
      (if (blank? photo)
        nil
        [:figure
         {:class "profile-picture",
          :style "float: right; max-width: 25%;"}
         [:img
          {:src
           (str "https://thermores.pwr.edu.pl/fcp/aGBUKOQtTKlQhbx08SlkTUgFFUWRuHQwFDBoIVURNWHVBG1gnBVcoFW8SBDRKHg/157/" photo)}]])
      [:dl
       {:id id,
        :class "pracownik"}
       (mapcat parse pairs)]]]))

(def process (comp box))
(def title [:h3 "Doktoranci"])
(println (str (h/html (concat [title] (map process doktoranci)))))
