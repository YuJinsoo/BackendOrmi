const babaYaga1 = {
  name: "John Wick",
  age: 53,
  from: "벨라루스",
  askingHim: function () {
    console.log("Yeah, I'm thinking I'm back!");
  },
};

//최신문법으로 function 키워드 없이 메소드 등록할 수 있습니다.
const babaYaga2 = {
  name: "John Wick",
  age: 53,
  from: "벨라루스",
  askingHim() {
    console.log("Yeah, I'm thinking I'm back!");
  },
};

// 키를 입력하지 않아도 변수명이 key 이름으로 자동으로 등록됩니다.
const a = "hello";
const b = "world";
const data = {
  a,
  b,
  c: "!!",
  d: [10, 20, 30],
};
data; //{a: 'hello', b: 'world', c: '!!', d: Array(3)}

// CRUD(Create, Read, Update, Delete)
// 데이터 추가(append), 데이터 업데이트(update)
const human = {
  name: "hojun",
  age: 98,
};

human.height = 250;
human["height"] = 250;
human; //{name: 'hojun', age: 98, height: 250}

human2 = {
  ...human,
  age: 10,
}; //{name: 'hojun', age: 10, height: 250}

// human.keys() // 이 메소드가 없습니다.
Object.keys(human); //(3) ['name', 'age', 'height']
Object.values(human); //(3) ['hojun', 98, 250]
Object.entries(human); //(3) [Array(2), Array(2), Array(2)]
