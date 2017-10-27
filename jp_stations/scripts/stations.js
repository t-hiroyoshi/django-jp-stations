const stations = require('../fixtures/stations.json');
const fs = require('fs')

const merged = stations.reduce((prev, next) => {
  const i = prev.findIndex(s => s.fields.name === next.station_name);

  if (i !== -1) {
    prev[i].fields.lines.push(next.line_cd);
  } else {
    prev.push({
      "model": "stations.Station",
      "pk": next.station_cd,
      "fields": {
        "name": next.station_name,
        "postal_code": next.post,
        "address": next.add,
        "latitude": next.lat,
        "longitude": next.lon,
        "status": next.e_status,
        "lines": [next.line_cd]
      }
    })
  }

  return prev
}, [])


fs.writeFile('../fixtures/converted_stations.json', JSON.stringify(merged, null, '  '));
