let arr = ["bananas", "apples", "oranges", "bananas"];

let dict = {};

for (let a of arr) {
  if (!dict.hasOwnProperty(a)) {
    dict[a] = 1;
  } else {
    dict[a] += 1;
  }
}

console.log(dict);
