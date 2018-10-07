function initMap() {
        var uluru = {lat: -25.363, lng: 131.044}, brisbane={lat:-27.470,lng:153.021};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
      }
initMap();
