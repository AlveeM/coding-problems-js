function limitedRepeat() {
  const interval = setInterval(() => {
    console.log("hi for now");
  }, 1000);

  setTimeout(() => clearInterval(interval), 5100);
}

limitedRepeat(); // should log (every second, for 5 seconds): hi for now