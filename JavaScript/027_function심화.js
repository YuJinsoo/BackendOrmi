// rest 문법
// 1. 매개변수에는 하나의 `rest`만 존재할 수 있습니다.
// 2. `rest`는 반드시 함수 정의의 마지막 매개변수여야 합니다.

function 함수2(a, b, ...c) {
  console.log(c);
  return Math.max(...c);
}

함수2("hello", "world", 10, 20, 30, 40);

function 함수2([a, b], ...c) {
  console.log(a);
  console.log(b);
  console.log(c);
}

함수2([1, 2], 10, 20, 30, 40);

//매개변수의 초기화
// 초기화는 할 수 있지만 순서를 바꿀 수 없습니다.
function 함수3(a = 10, b = 20, c = 30) {
  return a + b + c;
}

// 3020이 되어야 하는거 아니에요?
console.log(함수3((c = 1000), (a = 2000))); // 3030

//자바스크립트 scope
//스코프 체이닝. 변수가 없으면 상위 스코프에서 찾는 것이 반복적으로 일어남

// 함수 안에서도 밖의 변수를 참조하고 수정 할 있습니다.
// python과 다름. python은 참조 가능, 수정할 수 없음.
let z = 100;
function sum(x) {
  // x는 매개변수(parameter)이면서 지역변수(local val)
  let y = 50; // y는 지역변수
  z = z + y;
  return x + y;
}
console.log(sum(10)); // 10은 전달인자(argument)
// console.log(x); // 변수없음
// console.log(y); // 변수없음
console.log(z);
// 키워드로 인해 전역, 지역이 갈리는 것은 아닌지, let, var, const 모두 테스트 해보세요.

// 블록 레벨 스코프
if (true) {
  // for문이어도 마찬가지입니다.
  let x = 10;
  const y = 10;
}
console.log(x, y);

// 밖에 선언된 x는 함수 내부에서도 접근 가능합니다.
let x = 100;
function xplus() {
  x = x + 10;
  console.log(x);
}
xplus();
console.log(x);

// 함수 안에 함수
function a() {
  console.log("a 실행");
  function b() {
    console.log("b 실행");
  }
  b();
}

a();
// b() // Error

//블록레벨 스코프 연습
{
  let a = 10;
  const b = 10;
  console.log(a);
  console.log(b);
  {
    let a = 15;
    const b = 15;
    console.log(a);
    console.log(b);
    {
      let a = 20;
      const b = 20;
      console.log(a);
      console.log(b);
    }
  }
}

// 콜백함수
// 함수의 매개별수로 전달되어 실행되는 함수
// 함수에 아규먼트로 전달

function sum(x, y) {
  return x + y;
}

function custom(x, y, func) {
  return func(x, y);
}

custom(10, 20, sum);
// 콜백함수 예시
// let arr = [1,2,3]
// arr.sort(콜백함수)
// arr.filter(콜백함수)
// arr.map(콜백함수)

function f(x) {
  return x ** 2;
}
[1, 2, 3].map((x) => x ** 2);
[1, 2, 3].map(f);

//함수의 호이스팅(Hoisting)
// 함수가 호출 부분보다 밑에 있어도 에러를 뱉지 않고, 함수 선언을 최상단으로 끌어 올려지는 현상
// 변수와 함수의 호이스팅은 내용이 많습니다.
`
hello() # NameError: name 'hello' is not defined
def hello():
    print('hello world')
`;
hello();
function hello() {
  console.log("hello world");
}

//
// 즉시 실행 함수
// 익명 즉시 실행 함수
(function () {
  let a = 1;
  let b = 2;
  return a + b;
})();

// 기명 즉시 실행 함수
(function foo() {
  let a = 3;
  let b = 5;
  return a * b;
})();

foo(); // ReferenceError: foo is not defined
// 어차피 실행하지 못해서 의미가 없음.
// 메모리 효율적으로 관리하기 위해 바로 실행해야 하는 것들을 즉시 실행함수로 관리

// call by ~~

// array와 a가 가리키는 리스트가 같아서 내부 값 바뀜
let array = [100, 200, 300];
function test(a) {
  a[0] = 1000;
}
test(array);
array;

// v가 가리키는 값이 바뀌지 않음.
let v = 100;
function test(a) {
  a = 1000;
}
test(v);
v;
