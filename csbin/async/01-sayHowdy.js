function sayHowdy() {
  console.log('Howdy');
}

function testMe() {
  setTimeout(sayHowdy, 0);
  console.log('Partnah');
}

// 'Partnah'
// 'Howdy'
// After thinking it through, uncomment the following line to check your guess!
testMe(); // what order should these log out? Howdy or Partnah first?