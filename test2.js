let s1 = "abc";
let s2 = "cab";

let s3 = "bab";
let s4 = "aab";

function anagram(a, b) {
  let a1 = a.split().sort().join();
  let b1 = b.split().sort().join();
  return a1 === b1;
}

console.log(anagram(s3, s4));
