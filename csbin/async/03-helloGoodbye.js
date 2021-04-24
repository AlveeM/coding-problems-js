function helloGoodbye() {
  console.log("hello");
  setTimeout(() => {
    console.log("good bye")
  }, 3000);
}
helloGoodbye(); // should log: hello // should also log (after 3 seconds): good bye