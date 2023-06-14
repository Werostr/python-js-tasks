function show() {
  console.log("dsc");
  console.log(arguments);
}

show(1, 3, "t");

const obj = {
  name: "deeecode",
  age: 200,
  print: function () {
    function print2() {
      console.log(this);
    }

    print2();
  },
};

obj.print();
