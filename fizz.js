function fizzBuzz(n) {
  lista = [];
  for (let i = 1; i < n + 1; i++) {
    let s = "";
    if (i % 3 === 0) {
      s += "Fizz";
    }
    if (i % 5 === 0) {
      s += "Buzz";
    }
    lista.push(s);
  }
  return lista;
}

console.log(fizzBuzz(20));
