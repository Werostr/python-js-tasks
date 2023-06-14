let word = "111010";
let key = "10";

function cipher(x, k) {
  let result;
  for (let i = 0; i < x.length; i++) {
    if (x[i] === k[i % k.length]) {
      result += 0;
    }
  }
}
