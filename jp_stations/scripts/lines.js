const lines = require('../fixtures/lines.json');
const fs = require('fs')

const converted = lines.map(line => {
  return {
    "model": "stations.Line",
    "pk": line.line_cd,
    "fields": {
      "name": line.line_name_h,
      "status": line.e_status,
      "company": line.company_cd
    }
  };
})

fs.writeFile('../fixtures/converted_lines.json', JSON.stringify(converted, null, '  '));
