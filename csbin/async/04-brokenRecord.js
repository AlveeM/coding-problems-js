function brokenRecord() {
  setInterval(() => {
    console.log("hi again")
  }, 1000);
}

brokenRecord(); // should log (every second): hi again