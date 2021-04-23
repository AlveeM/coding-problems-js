function objectFilter(obj, callback) {
  return Object.keys(obj).reduce((res, key) => {
    if (obj[key] === callback(key)) {
      res[key] = obj[key];
    }
    return res;
  }, {})
}

const cities = {
London: 'LONDON',
LA: 'Los Angeles',
Paris: 'PARIS',
};
console.log(objectFilter(cities, city => city.toUpperCase())) // Should log { London: 'LONDON', Paris: 'PARIS'}