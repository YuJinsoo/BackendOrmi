// JSON
// - JSON.parse(): JSON문자열을 자바스크립트 객체로 변환합니다.
// - JSON.stringify() : 자바스크립트 객체를 JSON문자열로 변환합니다.

const json = '{"result":true, "count":42}';
const obj = JSON.parse(json);
console.log(obj);

const json2 = "[1,2,3]";
const obj2 = JSON.parse(json2);
console.log(obj2);

const json_obj = { result: true, count: 42 };
const s = JSON.stringify(json_obj);
s;

// JSON을 이용한 깊은 복사
let l = [10, 20, 30];
let a = JSON.parse(JSON.stringify(l));
a[0] = 1000;

console.log(l); // 깊은복사가 되었기 때문에 a[0]값이 바뀌지 않았음
