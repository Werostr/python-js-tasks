let test = "((((a+b) *c + (7-a)) – ((z+ 9)) – a) : 4 -z) + x ";

function brackets(dupa) {
  let equal = 0;
  for (let i = 0; i < dupa.length; i++) {
    if (dupa[i] === "(") {
      equal++;
    } else if (dupa[i] === ")") {
      equal--;
      if (equal < 0) return false;
    }
  }
  console.log(equal);
  return !equal;
}

console.log(brackets(test));
