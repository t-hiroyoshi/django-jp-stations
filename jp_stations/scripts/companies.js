const companies = require('../fixtures/companies.json');
const fs = require('fs')

const converted = companies.map(company => {
  return {
    "model": "stations.Company",
    "pk": company.company_cd,
    "fields": {
      "name": company.company_name,
      "status": company.e_status
    }
  };
})

fs.writeFile('../fixtures/converted_companies.json', JSON.stringify(converted, null, '  '));
