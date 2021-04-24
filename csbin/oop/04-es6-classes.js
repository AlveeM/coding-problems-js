/*** CHALLENGE 8 ***/

class PersonClass {
	constructor(name) {
    this.name = name;
	}

  greet() {
    console.log("hello")
  }

}


// /********* Uncomment this line to test your work! *********/
const george = new PersonClass;
// george.greet(); // -> Logs 'hello'



/*** CHALLENGE 9 ***/

class DeveloperClass extends PersonClass {
  introduce() {
    console.log(`Hello World, my name is ${this.name}`);
  }
}

// /********* Uncomment these lines to test your work! *********/
const thai = new DeveloperClass('Thai', 32);
console.log(thai.name); // -> Logs 'Thai'
thai.introduce(); //-> Logs 'Hello World, my name is Thai'