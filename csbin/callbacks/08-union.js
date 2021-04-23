function union(...arrays) {
	return arrays.reduce((acc, arr) => {
      arr.forEach(el => {
          if (!acc.includes(el)) {
              acc.push(el);
          }
      });
      return acc;
  })
}