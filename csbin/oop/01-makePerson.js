function makePerson(name, age) {
  return {
    name,
    age,
  }
}

const vicky = makePerson('Vicky', 24);
console.log(vicky.name); // -> Logs 'Vicky'
console.log(vicky.age); // -> Logs 24