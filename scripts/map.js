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
        src: "https://cdn.jsdelivr.net/gh/dawidsowa/Automatyzacja-Thermores/imgs/marker.png",
      }),
    }),
  });
  map.addLayer(markers);

  var marker = new ol.Feature(new ol.geom.Point(ol.proj.fromLonLat(pos)));
  markers.getSource().addFeature(marker);
});
