// nullish 연산자 ??
// https://ko.javascript.info/nullish-coalescing-operator
// 나온지 얼마 되지 않았기 때문에 선임이 모를 수 있습니다.
// IE는 지원하지 않습니다.

//중간에 하나라도 값이 들어있다면 그 값을 출력합니다.
let firstname = null;
let lastname = null;
let nickname = "licat";

firstname ?? lastname ?? nickname ?? "익명의 사용자"; // 'licat'

let a = null;
let b = 10;
let c = null;

a ?? 100; // a가 null인지 물어보고, null이면 100을 넣겠다!
a ?? b; //10
a ?? b ?? c; //=> (a ?? b) ?? c 이기 때문에 a, b가 값이 있다면 의미없음

// nullish 연산자와 단락평가의 차이점
let height = 0;

height || 100; // 100
height ?? 100; // 0 // 0은 null이 아니니깐 0출력

let width = NaN;

width || 100; // 100
width ?? 100; // NaN

// 단락평가의 || : 0, null, undefined, '', NaN를 false로 판단합니다.
// ??           : null, undefined
