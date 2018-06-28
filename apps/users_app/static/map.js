
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
    	zoom: 8,
        // center: {lat: -34.397, lng: 150.644}
});
var geocoder = new google.maps.Geocoder();

var places = document.getElementsByClassName('address');
for(var i = 0; i < places.length; i++){
	// geocodeAddress(geocoder, map, place);
	codeAddress(places[i].innerText)
}

function codeAddress(address) {
    var address = address
    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == 'OK') {
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location
        });
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
  }
}

// function geocodeAddress(geocoder, resultsMap, place) {
//         var address = place
//         geocoder.geocode({'address': place}, function(results, status) {
//           if (status === 'OK') { 
//             var marker = new google.maps.Marker({
//               map: resultsMap,
//               position: results[0].geometry.location
//             });
//             resultsMap.setCenter(results[0].geometry.location);
//           } else {
//             alert('Geocode was not successful for the following reason: ' + status);
//           }
//         });
//       }
//   }

    




// function initMap() {
// var locations = [
//     ['Philz Coffee<br>\
//     801 S Hope St A, Los Angeles, CA 90017<br>\
//    <a href="https://goo.gl/maps/L8ETMBt7cRA2">Get Directions</a>', 34.046438, -118.259653],
//     ['Philz Coffee<br>\
//     525 Santa Monica Blvd, Santa Monica, CA 90401<br>\
//    <a href="https://goo.gl/maps/PY1abQhuW9C2">Get Directions</a>', 34.017951, -118.493567],
//     ['Philz Coffee<br>\
//     146 South Lake Avenue #106, At Shoppers Lane, Pasadena, CA 91101<br>\
//     <a href="https://goo.gl/maps/eUmyNuMyYNN2">Get Directions</a>', 34.143073, -118.132040],
//     ['Philz Coffee<br>\
//     21016 Pacific Coast Hwy, Huntington Beach, CA 92648<br>\
//     <a href="https://goo.gl/maps/Cp2TZoeGCXw">Get Directions</a>', 33.655199, -117.998640],
//     ['Philz Coffee<br>\
//     252 S Brand Blvd, Glendale, CA 91204<br>\
//    <a href="https://goo.gl/maps/WDr2ef3ccVz">Get Directions</a>', 34.142823, -118.254569]
//   ];

//   var center = {lat: 33.628342, lng: -117.927933};
//   var map = new google.maps.Map(document.getElementById('map'), {
//     zoom: 10,
//     center: center
//   });

//   var infowindow =  new google.maps.InfoWindow({});
// var marker, count;
// for (count = 0; count < locations.length; count++) {
//     marker = new google.maps.Marker({
//       position: new google.maps.LatLng(locations[count][1], locations[count][2]),
//       map: map,
//       title: locations[count][0]
//     });
// google.maps.event.addListener(marker, 'click', (function (marker, count) {
//       return function () {
//         infowindow.setContent(locations[count][0]);
//         infowindow.open(map, marker);
//       }
//     })(marker, count));
// }
// }