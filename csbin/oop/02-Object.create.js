/*** CHALLENGE 2 ***/

const personStore = {
  greet() {
		console.log("hello");
	}
};

// /********* Uncomment this line to test your work! *********/
// personStore.greet(); // -> Logs 'hello'



/*** CHALLENGE 3 ***/

function personFromPersonStore(name, age) {
	const person = Object.create(personStore);
	person.name = name;
	person.age = age;
	return person;
}

const sandra = personFromPersonStore('Sandra', 26);


// /********* Uncomment these lines to test your work! *********/
// console.log(sandra.name); // -> Logs 'Sandra'
// console.log(sandra.age); //-> Logs 26
// sandra.greet(); //-> Logs 'hello'



/*** CHALLENGE 4 ***/

// add code here
personStore.introduce = function() {
	console.log(`Hi, my name is ${this.name}`)
}

sandra.introduce(); // -> Logs 'Hi, my name is Sandra'