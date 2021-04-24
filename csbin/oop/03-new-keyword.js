/*** CHALLENGE 5 ***/

function PersonConstructor() {
	this.greet = function() {
    console.log('"hello');
  }
}


// /********* Uncomment this line to test your work! *********/
const simon = new PersonConstructor;
// simon.greet(); // -> Logs 'hello'



/*** CHALLENGE 6 ***/

function personFromConstructor(name, age) {
  const person = new PersonConstructor();
  person.name = name;
  person.age = age;
  return person;
}

const mike = personFromConstructor('Mike', 30);


// /********* Uncomment these lines to test your work! *********/
// console.log(mike.name); // -> Logs 'Mike'
// console.log(mike.age); //-> Logs 30
// mike.greet(); //-> Logs 'hello'



/*** CHALLENGE 7 ***/
// add code here
PersonConstructor.prototype.introduce = function() {
  console.log(`Hi, my name is ${this.name}`);
}

mike.introduce(); // -> Logs 'Hi, my name is Mike'