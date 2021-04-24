class SecondClock {
  constructor(cb) {
    this.cb = cb;
  }

  start() {
    let seconds = 1;
    this.timer = setInterval(() => {
      this.cb(seconds);
      seconds++;
    }, 1000);
  }

  reset() {
    clearInterval(this.timer);
  }
}

const clock = new SecondClock((val) => { console.log(val) });
console.log("Started Clock.");
clock.start();
setTimeout(() => {
    clock.reset();
    console.log("Stopped Clock after 6 seconds.");
}, 6000);