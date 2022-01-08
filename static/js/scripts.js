let x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    let username = $('#username').val();
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;
    x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
    $.post("api/v1/location/",
        {
            username: username,
            latitude: latitude,
            longitude: longitude
        },
        function (data, status) {
            console.log(status);
        });

}