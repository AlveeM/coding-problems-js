function everyXsecsForYsecs(func, interval, duration) {
  const timer = setInterval(() => func(), interval);
  setTimeout(() => clearInterval(timer), duration);
}
// Uncomment the following lines to check your work!
function theEnd() {
  console.log('This is the end!');
}
// everyXsecsForYsecs(theEnd, 2, 20); // should invoke theEnd function every 2 seconds, for 20 seconds): This is the end!
everyXsecsForYsecs(theEnd, 1000, 5000);