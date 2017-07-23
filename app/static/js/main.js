/**
 * Created by carson on 7/2/17.
 */
var map; //Leaflet map
var tilesLoaded = false; //Boolean used to wait for tiles to load before taking screengrab.

$(document).ready(function () {
    initMap();
});
$(window).on("resize", function () { $("#mapid").height($(window).height()-80);
map.invalidateSize(); }).trigger("resize");

/**
 * Leaflet function to initialize map
 * with tile set, etc.
 */
function initMap() {
    map = L.map('mapid').setView([40.060620, -77.523182], 17);
    L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        maxZoom: 18,
        id: 'streets-v9',
        accessToken: 'pk.eyJ1IjoiY2Fyc253ZCIsImEiOiJjajRtN3JycmExM2Y1MnhucnJqdXhxZzc3In0.qdhlOuL5yocMtpVQx_51bA'
    }).addTo(map);
    tilesLoaded = true;
    $("#mapid").trigger("resize")
}