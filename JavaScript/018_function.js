function f(x, y) {
  return x + y;
}

// 즉시실행함수.
// 정의와 동시에 실행되는 함수
(function () {
  console.log("Hello");
});

// arrow function
(x, y) => x + y;

//python에서는 lambda의 위상이 재사용하지 않는 함수에서 많이 사용하지만
// JavaScript에서는 화살표 함수가 일반함수만큼 자주사용됩니다.
// (화살표 함수의 문법이 나온 지 그렇게 오래되지 않았습니다.)

//1.중괄호가 없고 함수가 return되는 코드1줄이면 return 생략합니다.
let f2 = (x, y) => x + y; // 변수에 할당할 수 있습니다.
f2(10, 20); // 30

//2.중괄호를 쓰면 return 이 있어야 합니다.
let f3 = (x, y) => {
  let z = x + y;
  return z;
};

//3. 전달하는 파라미터가 1개이면 소괄호도 생략할 수 있습니다.
let f4 = (x) => x + x;
f4(2); //4

// 반지름이 입력되면 원의 넓이를 구하는 화살표 함수를 만들어주세요. 가능하면 가장 단축된 방법으로
let f5 = (x) => Math.PI * x * x;
f5(10);

// 다음처럼 여러 값이 입력되었을 때, 가장 큰 값과 가장 작은 값, 총합을 충력하는 함수를 만들어주세요
function f6(a, b, c, d) {
  max = Math.max(a, b, c, d);
  min = Math.min(a, b, c, d);
  sum = a + b + c + d;
  return [max, min, sum];
}

let f7 = (a, b, c, d) => {
  max = Math.max(a, b, c, d);
  min = Math.min(a, b, c, d);
  sum = a + b + c + d;
  return [max, min, sum];
};
