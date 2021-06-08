function dateStamp(func) {
  return function(...args) {
      let today = new Date();
      return {
          date: today.toDateString(),
          output: func(...args)
      }
  }
}
const stampedMultBy2 = dateStamp(n => n * 2);
console.log(stampedMultBy2(4)); // => should log { date: (today's date), output: 8 }
console.log(stampedMultBy2(6)); // => should log { date: (today's date), output: 12 }