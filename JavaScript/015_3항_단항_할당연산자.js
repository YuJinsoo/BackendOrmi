// 단항 연산자
// 할당 연산자
// 3항연산자

// 단항연산자
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Operator_Precedence
// python에는 지원하지 않는 문법입니다.
// 증감연산, 단항연산
let a = 10;
// 둘 다 a를 1 만큼 증가시키는 코드
a++; // 선할당 후증가. 출력하고 증가시킴
++a; // 선증가 후할당. 증가시키고 보여줌
+"10"; //10
typeof +"10"; //number
+"10" + 10; //20

//++ 위치 바꿔도 달라지지 않습니다.
for (let i = 0; i < 10; i++) {
  console.log(i);
}

// 할당연산자
a = 10;
a += 5;
a /= 5;

// 3항 연산자
// 조건식 ? 조건식이 참일 때 실행될 코드 : 조건식이 거짓일 때 실행될 코드

let x = true ? 100 : 200; // x 는 100
let y = false ? 100 : 200; // y 는 200

// 아래 2개의 3항 연산자를 합치면...
let aa = false ? 100 : 200;
let bb = true ? 10 : 20;
false ? 100 : true ? 10 : 20;

// 예제 error가 나지 않는 코드, 한을 영어 숫자 등등
let sortedData = jsonData.sort((a, b) =>
  a[key] > b[key] ? -1 : a[key] < b[key] ? 1 : 0
);

//아래와 같이 변수할당 없이 바로 3항 연산자로 return 가능합니다.
function solution(n) {
  return Math.sqrt(n) === Math.floor(Math.sqrt(n)) ? 1 : 2;
}

// 3항 연산자의 예제
const factorial = (num) => (num === 0 ? 1 : num * factorial(num - 1));

// lv0 컨트롤 제트
//  https://school.programmers.co.kr/learn/courses/30/lessons/120853
function solution(s) {
  s = s.split(" ");
  let arr = [];
  for (let v of s) v === "Z" ? (arr.length ? arr.pop() : "") : arr.push(v);
  return arr.reduce((a, v) => a + +v, 0);
}
