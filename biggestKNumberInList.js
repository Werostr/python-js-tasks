var n = [1, 7, 9, 5, 4, 7, 4, 3];
// [9,7,7,5,4,4,3,1]
// [9,7,4,4,3,1,-5,-7]
var k = 4;

function córcia(n, k) {
  let pivot_index = Math.floor(Math.random() * n.length);
  let pivot = n[pivot_index];
  let less = [];
  let more = [];

  for (let i = 0; i < n.length; i++) {
    if (i === pivot_index) {
      continue;
    }
    if (n[i] < pivot) {
      less.push(n[i]);
    } else {
      more.push(n[i]);
    }
  }

  if (more.length === k - 1) {
    return pivot;
  } else if (more.length > k - 1) {
    return córcia(more, k);
  } else {
    return córcia(less, k - more.length - 1);
  }
}

console.log(córcia(n, k));
