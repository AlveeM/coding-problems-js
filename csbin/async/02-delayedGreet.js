function delayedGreet() {
  setTimeout(() => {
    console.log("welcome")
  }, 3000);
}
delayedGreet(); // should log (after 3 seconds): welcome