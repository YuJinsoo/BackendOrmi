// https://codingdojang.com/scode/393?answer_mode=hide

// python
// str(list(range(10001)))count('8')

//javascript
// 이 코드는 알고리즘 문제 풀이할때만 쓰세요.
".".repeat(100);
".".repeat(100).split("."); // 101개..

// 1
"."
  .repeat(99)
  .split(".")
  .map((v, i) => i + 1)
  .join("")
  .split("")
  .filter((v) => v === "8").length;

// 2
s = "";
for (let i = 0; i < 101; i++) {
  s += i;
}
s.split("").filter((v) => v === "8").length;

//3
Array(101)
  .fill(0)
  .map((v, i) => "" + i) // 안에서 메서드체이닝을 더 할수 있지만 복잡도가 상상할 것 같아 실행하지 않았습니다.
  .join("")
  .split("")
  .filter((v) => v === "8").length;

//문제9 가장 거리가 짧은 것의 쌍을 출력하는 함수
let a = [10, 20, 30, 40];
let b = [100, 200, 300, 400];
let c = [1000, 2000, 3000, 4000];
a.map((v, i) => [v, b[i]]);
a.map((v, i) => [v, b[i], c[i]]);

//1
const zip = (a, b) => a.map((v, i) => [v, b[i]]);

let s = [1, 3, 4, 8, 13, 17, 20];
zip(s, s.slice(1)); // slice(1) 이면 1번 인덱스부터 끝까지
zip(s, s.slice(1)).sort((a, b) => a[1] - a[0] - (b[1] - b[0])); // a가 더 큰 인덱스... b가 a의 이전인덱스 값
zip(s, s.slice(1)).sort((a, b) => a[1] - a[0] - (b[1] - b[0]))[0];

//2

s = [1, 3, 4, 8, 13, 17, 20];
for (let i = 0; i < s.length; i++) {
  console.log(s[i]);
}
//초급자가 이해하기 쉬운코드
s = [1, 3, 4, 8, 13, 17, 20];
for (let i = 1; i < s.length; i++) {
  console.log(s[i] - s[i - 1]);
}

//일반적인 방법
s = [1, 3, 4, 8, 13, 17, 20];
let index = 0;
// 최솟값을 찾아내려면 먼저 최댓값을 저장해라!
// 최댓값을 찾아내려면 먼저 최솟값을 저장해라!
let min = -Infinity;
for (let i = 0; i < s.length - 1; i++) {
  if (s[i + 1] - s[i] < min) {
    min = s[i + 1] - s[i];
    index = i;
  }
}
console.log(s[index], s[index + 1]);

//문제10
// 엘리베이터 최대 몸무게는 500kg 입니다.
// 다음 친구들이 엘리베이터를 탔을 때 최대로 탑승할 수 있는 인원수를 구하세요.
let weight = [60, 50, 55, 60, 77, 88, 56, 67, 89, 45, 55, 44];
weight.sort((a, b) => a - b);
let total = 0;
let num = 0;
for (let i = 0; i < weight.length; i++) {
  if (total < 500) {
    num += 1;
    total += weight[i];
  } else {
    num -= 1;
    break;
  }
}
num;

//강사님풀이
sum = 0;
count = 0;
for (const i of weight) {
  sum += i;
  if (sum >= 500) {
    break;
  }
  count += 1;
}

// python의 zip
// const zip = (a, b) => a.map((v, i) => [v, b[i]]);
// python의 map
const map = (func, iter) => {
  result = [];
  for (const i of iter) {
    result.push(func(i));
  }
  return result;
};
