function letterCount(text) {
  let maxCounter = 0;
  let maxletter = 0;
  let dictio = {};
  for (const letter of text) {
    if (letter in dictio) {
      dictio[letter] += 1;
    } else {
      dictio[letter] = 1;
    }
    if (dictio[letter] > maxCounter) {
      maxCounter = dictio[letter];
      maxletter = letter;
    }
  }
  return [maxletter, maxCounter];
}

console.log(letterCount("kehrfiehvwihvilqevbrlewhviebvhv"));
