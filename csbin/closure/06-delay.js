function delay(func, wait, ...args) {
  return function() {
    setTimeout(() => func(...args), wait);
  }
}