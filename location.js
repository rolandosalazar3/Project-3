var data = [{type: 'densitymapbox', lon: [-74.6591, -71.113, -87.6012, -72.9234, -73.9613, -122.169, -71.0935, -78.9403, -75.1624, -76.6096], lat: [40.3499, 42.3747, 41.7902, 41.314, 40.8065, 37.4314,42.359, 36.0014, 39.9523, 39.2906], z: [1, 2, 3, 3, 5, 5, 7, 8, 8, 10]}];

var layout = {width: 1600, height: 1200, mapbox: {style: 'stamen-terrain'}};

Plotly.newPlot('myDiv', data, layout);