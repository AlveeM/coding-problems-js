function createSecretHolder(secret) {
  let secretVal = secret;
  return{
    getSecret() {
      return secretVal;
    },
    setSecret(newSecret) {
      secretVal = newSecret;
    }
  }
}

obj = createSecretHolder(5)
console.log(obj.getSecret()) // => returns 5
obj.setSecret(2)
console.log(obj.getSecret()) // => returns 2
