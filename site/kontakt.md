```{=html}
<script type="text/javascript">
  // <![CDATA[
  var head = document.head;
  var link = document.createElement("link");
  link.type = "text/css";
  link.rel = "stylesheet";
  link.href = "https://cdn.jsdelivr.net/gh/dawidsowa/Automatyzacja-Thermores/style.css";
  head.appendChild(link);
  // ]]>
</script>
```

:::::: cols
::: col

Politechnika Wrocławska\
Wydział Mechaniczno-Energetyczny\
**Katedra Termodynamiki i Odnawialnych Źródeł Energii**\
Wybrzeże Wyspiańskiego 27\
50-370 Wrocław

### Kierownik Katedry

Sławomir Pietrowicz\
tel. 71/ 320 36 17\
budynek D-2, pok. 11B\
e-mail: [slawomir.pietrowicz@pwr.edu.pl](mailto:slawomir.pietrowicz@pwr.edu.pl)

### Administrator strony

Dawid Sowa\
e-mail: [dawid.sowa@pwr.edu.pl](mailto:dawid.sowa@pwr.edu.pl)

:::
::: col

```{=html}
<script
  type="text/javascript"
  src="https://cdn.jsdelivr.net/npm/ol/dist/ol.js"
></script>
<div id="map" class="map" style="height: 20em; width: 100%;"></div>
<script type="text/javascript">
  // <![CDATA[
  var head = document.head;
  var link = document.createElement("link");

  link.type = "text/css";
  link.rel = "stylesheet";
  link.href = "https://cdn.jsdelivr.net/npm/ol/ol.css";
  head.appendChild(link);

  $(window).bind("load", function () {
    var pos = [17.057231970115808, 51.11012582273214];

    var map = new ol.Map({
      target: "map",
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM(),
        }),
      ],
      view: new ol.View({
        center: ol.proj.fromLonLat(pos),
        zoom: 16,
      }),
    });

    var markers = new ol.layer.Vector({
      source: new ol.source.Vector(),
      style: new ol.style.Style({
        image: new ol.style.Icon({
          anchor: [0.5, 1],
          src: "https://github.com/moovspace/map-marker-openlayers/raw/master/img/marker.png",
        }),
      }),
    });
    map.addLayer(markers);

    var marker = new ol.Feature(new ol.geom.Point(ol.proj.fromLonLat(pos)));
    markers.getSource().addFeature(marker);
  });
  // ]]>
</script>
```

:::
::::::
