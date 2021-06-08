function censor() {
  const cache = {}
  return function (str1, str2) {
		if (str2) {
    	cache[str1] = str2;
  	} else {
      Object.keys(cache).forEach(key => {
        str1 = str1.replace(key, cache[key]);
      })
      return str1;
    }
  }
}

const changeScene = censor();
changeScene('dogs', 'cats');
changeScene('quick', 'slow');
console.log(changeScene('The quick, brown fox jumps over the lazy dogs.')); // => should log 'The slow, brown fox jumps over the lazy cats.'