//python dictionary와의 차이점
// javascript에서는 key값에 따옴표가 없을 경우 자동으로 문자열로 변환해줍니다.
// true, false 값은 앞에 대소문자가 다릅니다.
let obj = {
  id: "licat",
  pw: "1234",
  name: "leehojun",
  email: "hojun@gamil.co.kr",
  active: false,
};

obj["id"];
obj.id; //python에서는 error
// obj.'id'; // error

let a = 10;
let b = 10;
let c = 10;
let d = { a, b, c }; // 자동으로 object로 바꿔줌
d; // {a: 10, b: 10, c: 10}

// 유사배열 객체. 배열과 유사하지만 배열은 아닙니다.
let txt = {
  0: "h",
  1: "e",
  2: "l",
  3: "l",
  4: "o",
};

txt[0];
txt[1];
txt[2];
// txt.0; //error

// value의 값으로 문자열 외에 다른 값을 넣었을 경우
let test = {
  one: sum,
  two: console.log,
  three: window.innerWidth,
  four: [10, 20, 30],
  five: "10",
  six: 100,
};
console.log(test);
test.two("호준!!");

// object에서 바로 데이터를 뽑아낼 수 없습니다..
let user = {
  id: "licat",
  pw: "1234",
  name: "leehojun",
  email: "hojun@gmail.co.kr",
  active: false,
};
console.log(Object.keys(user)); // (5) ['id', 'pw', 'name', 'email', 'active']
console.log(Object.values(user)); // VM728:9 (5) ['licat', '1234', 'leehojun', 'hojun@gmail.co.kr', false]
console.log(Object.entries(user)); // VM728:10 (5) [Array(2), Array(2), Array(2), Array(2), Array(2)]

// user.keys() 이런식으로 동작하지 않습니다.
// why? 여기에 포함시킬수 없는 결정적이 이유가 있습니다.
// object를 상속받는 곳이 많습니다.
// 그래서 Map이라는 자료형이 추가로 등장함
