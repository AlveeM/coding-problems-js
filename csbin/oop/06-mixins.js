class Dog {
  constructor() {
    this.legs = 4;
  }
  speak() {
    console.log('Woof!');
  }
}

const robotMixin = {
  skin: 'metal',
  speak: function() { console.log(`I have ${this.legs} legs and am made of ${this.skin}`) },
}

let robotFido = new Dog();

// robotFido = /* Put code here to give Fido robot skills */;
robotFido = Object.assign(robotFido, robotMixin);


// /********* Uncomment to test your work! *********/
robotFido.speak() // -> Logs "I am made of metal"