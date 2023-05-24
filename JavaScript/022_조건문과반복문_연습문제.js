//1부터 100까지 더하는 예제
// 1
let s = 0;
for (let i = 1; i < 101; i++) {
  s += i;
}
s;

//2
let s2 = 0;
let i = 1;
while (i < 101) {
  s2 += i;
  i++;
}
s2;

new Array(10); //(10) [empty × 10]
new Array(10).fill(1);
// fill 없으면 empty로 생성됩니다.
new Array(10).map((_, i) => i); // (10) [empty × 10]
new Array(10).fill(1).map((_, i) => i); // (10) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new Array(10).fill(1).map((_, i) => i + 1); // (10) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new Array(100).fill(1).map((_, i) => i + 1);

//3
let range = new Array(100).fill(1).map((_, i) => i + 1);
let s3 = 0;
for (const i of range) {
  //   console.log(i);
  s3 += i;
}
s3;

//4
new Array(100)
  .fill(1)
  .map((_, i) => i + 1)
  .reduce((a, c) => a + c, 0);

//5
let range2 = new Array(100).fill(1);
let s4 = 0;
for (const index in range2) {
  // index가 문자열이라서 변환해준겁니다.
  // s4 += +index +1
  s4 += parseInt(index) + 1;
}
s4;

//1부터 100까지 짝수만 더하는 예제
//1
let ss = 0;
for (let i = 1; i < 101; i++) {
  if (i % 2 === 0) {
    ss += i;
  }
}
ss;

//2 반복횟수가 적어 더 효율적
let ss2 = 0;
for (let i = 0; i < 101; i += 2) {
  if (i % 2 === 0) {
    ss2 += i;
  }
}
ss2;

//3
let ss3 = 0;
let ii = 0;
while (ii < 101) {
  if (ii % 2 == 0) {
    ss3 += ii;
  }
  ii++;
}
ss3;

// [10, 5, 4, 7, 9, 3, 2, 5, 4, 7, 4, 2, 1]에서 5보다 작은 수만 다 더해주세요
let ar = [10, 5, 4, 7, 9, 3, 2, 5, 4, 7, 4, 2, 1];
//1
ar.filter((v) => v < 5).reduce((a, b) => a + b, 0);
//2
ss4 = 0;
for (const i of ar) {
  if (i < 5) {
    ss4 += i;
  }
}

//3
let ii2 = 0;
let ss5 = 0;
while (ii2 < ar.length) {
  if (ar[ii2] < 5) {
    ss5 += ar[ii2];
  }
  ii2++;
}
ss5;

//4 map은 function의 값 그대로 Array에 추가하기 때문에...
// v < 5로 하면 true, false만 반환됨. 그래서 3항연산자 쓰면 됨.
ar.map((v) => (v < 5 ? v : 0)).reduce((a, c) => a + c, 0);
ar.map((v) => {
  if (v < 5) {
    return v;
  }
  return 0;
}).reduce((a, c) => a + c, 0);

//5 reduce만 풀기. 매우 어려운 방법입니다.
ar.reduce((a, c) => (c < 5 ? a + c : a), 0);

//6 forEach()
let ss6 = 0;
ar.forEach((v) => v < 5 && (ss6 += v));
ss6;

// [10, '5', 4, '7', 9, '3', 2, '5', 4, '7', '4', '2', '1']에서 모든 숫자를 다 더해주세요.
// 다양하게 풀어보세요. for, while, filter, map, reduce...
let a = [10, "5", 4, "7", 9, "3", 2, "5", 4, "7", "4", "2", "1"];

let sss = 0;
for (const i of a) {
  if (typeof i == "number") {
    sss += i;
  }
}

a.filter((v) => typeof v === "number").reduce((a, c) => a + c, 0);

a.map((v) => (typeof v === "number" ? v : 0)).reduce((a, c) => a + c, 0);

sss = 0;
a.forEach((v) => typeof v === "number" && (sss += v));
sss;

//
sss = 0;
for (const i of a) {
  if (typeof i == "number") {
    sss += i;
  }
}
sss;

//보통 type check를 typeof()로 하지는 않습니다....
// 아래같이 쓰면 확실합니다.
function typeCheck(value) {
  return Object.prototype.toString.call(value).slice(8, -1);
}
// typeCheck([1,2,3])
// Array // '[object Array]'이렇게 나와서 slice해줌
// typeof([1,2,3])
// 'object'

sss = 0;
iii = 0;
while (iii < a.length) {
  if (typeof a[iii] === "number") {
    sss += a[iii];
  }
  iii++;
}
sss;

///난이도가 있습니다.
a.reduce((a, c) => (typeof c === "number" ? a + c : a), 0);

//number와 string을 모두 더하는 것이었다면?
a.reduce((a, c) => a + +c, 0);
a.reduce((a, c) => a + parseInt(c), 0);
a.map((v) => parseInt(v)).reduce((a, c) => a + c, 0);

//모음제거
//https://school.programmers.co.kr/learn/courses/30/lessons/120849

new Array("hello world");
"hello world".split(" ");
Array.from("hello world"); // (11) ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

Array.from("hello world")
  .filter((v) => !["a", "e", "i", "o", "u"].includes(v))
  .join("");

function solution(my_string) {
  return Array.from("my_string")
    .filter((v) => !["a", "e", "i", "o", "u"].includes(v))
    .join("");
}

function solution(my_string) {
  let result = "";
  for (const s of my_string) {
    if (["a", "e", "i", "o", "u"].includes(s)) {
      continue;
    }
    result += s;
  }
  return result;
}

// 쉬운문제
// 용돈은 매년 2배씩 오릅니다.
// 올해 받은 용돈은 10000원입니다.
// 나이는 8살입니다.
// 30만원 이상이 되면 용돈이 더이상 오르지 않습니다.
// for와 continue 문법을 써서 8살 부터 35까지 받은 용돈의 총합을 구하세요.

k = 10000;
total = 0;
for (let i = 8; i <= 35; i++) {
  k = k >= 300000 ? k : k * 2;
  total += k;
}
total;

// 문제 2
// https://school.programmers.co.kr/learn/courses/30/lessons/120850?language=javascript
// isNan()에 문자를 넣으면 true, 숫자는 false가 나옵니다.
function solution(my_string) {
  my_string
    .split("")
    .filter((v) => !isNaN(v))
    .map((v) => +v) //v *1 해도 숫자로 바뀜
    .sort((a, b) => a - b);
}
