function intersection(...arrays) {
  return arrays.reduce((acc, arr) => {
    return acc.filter(el => arr.includes(el));
  })
}

console.log(intersection([5, 10, 15, 20], [15, 20, 88, 1, 5, 7], [1, 10, 15, 5]));
// should log: [5, 15]
