const arr1 = [];
const arr2 = [1, 2, 3];
const arr3 = new Array(4, 5, 6);

// const arr3 = new Array(3);

const arr = [[10, 20], 2, 3, 4, 5];
arr[0];
arr[0][0];
arr.length;
arr.pop(); //5
arr.pop(2); //아규먼트 값과 상관없이 마지막 값을 꺼냅니다.
arr; //[[10, 20], 2, 3, 4 ];
arr.push(100); //5
arr; // (5) [Array(2), 2, 3, 4, 100]

// shift는 앞에서 값을 꺼내고, unshift는 앞에다 값을 추가합니다.
const arr4 = [1, 2, 3, 4, 5];
arr4.shift(); //1
arr4; // [2, 3, 4, 5];
arr4.unshift(100); //5
arr4; //(5) [Array(2), 2, 3, 4, 100]
arr4.unshift(1000, 2000, 3000); //8
arr4; //(8) [1000, 2000, 3000, 100, 2, 3, 4, 5]

//splice
// splice() 메소드는 배열의 요소를 추가, 제거 또는 교체
// array.splice(start, deleteCount, changeitem)
const arr5 = [1, 2, 3, 4, 5];
arr5.splice(1, 0, 100);
arr5; //(6) [1, 100, 2, 3, 4, 5]

arr5.splice(1, 1, 100);
arr5; //(5) [1, 100, 3, 4, 5]

arr5.splice(1, 1, 10000, 20000);
arr5;

//slice
const arr6 = [10, 20, 30, 40, 50, 60];
arr6.slice(2, 5); // (3) [30, 40, 50]

//sort
// 문자열 정렬처럼 사전식으로 정렬합니다. 1 11 2 22 ...
const arr7 = [1, 11, 2, 3, 7, 22, 8, 5];
// 오름차순
arr7.sort((a, b) => a - b);
// 내림차순
arr7.sort((a, b) => b - a);

// 자주사용합니다. forEach()
// forEach()는 반복만 합니다!
// 새로운 array를 만들고 싶다면 map을 사용해주세요.
const arr8 = [1, 11, 2, 3, 7, 22, 8, 5];
arr8.forEach((item, index, ar) => {
  console.log(item);
  console.log(index);
  console.log(ar);
});
// 필요없는건 안받아도 됨.
arr8.forEach((v, i) => {
  console.log(v); // value
  console.log(i); // index
});

/*
<body>
    <div id="0"></div>
    <div id="1"></div>
    <div id="2"></div>
    <div id="3"></div>
    <div id="4"></div>
    <div id="5"></div>
    <div id="6"></div>
    <div id="7"></div>
</body>
*/
const arr9 = [1, 11, 2, 3, 7, 22, 8, 5];
arr9.forEach((v, i) => {
  const tag = document.getElementById(i);
  tag.innerHTML = v;
});

//NodeList 는 IE에서 지원하지 않음.. 주의해야함
//NodeList에서 forEach안됨?
document.body.childNodes; // NodeList

//filter
const arr10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const newArr = arr10.filter((el) => el % 2 === 0);

console.log(newArr);

//reduce
[10, 20, 30, 40].reduce((a, c) => {
  console.log(a, c);
  return a + c;
});

[10, 20, 30, 40].reduce((a, c) => a + c, 0);
[].reduce((a, c) => a + c, 0);
[].reduce((a, c) => a + c); // 견고하지 못한 코드입니다.

//include
// 10 in [10,20,30,40,50]; // 이런 문법 없습니다.
// 여기서 in 앞에 나오는 값은 key(index) 입니다.
10 in [1, 2, 3, 4]; //false;
1 in [1, 2, 3, 4]; // true;
2 in [1, 2, 3, 4]; // true;
3 in [1, 2, 3, 4]; // true;
4 in [1, 2, 3, 4]; // false;

"one" in { one: 1, two: 2 }; // true;

[10, 20, 30, 40].includes(10); // true;

// join
const arr11 = ["hello", "world", "hojun"];
arr11.join("!"); // hello!world!hojun

// map
// python의 map과 같다.
// map은 아래 형태보다 데이터를 뽑아내는 형태로 많이 사용합니다.
// Array를 반환합니다!
[1, 2, 3, 4].map((x) => x ** 2); //(4) [1, 4, 9, 16]

[
  [10, 20],
  [20, 30],
  [30, 40],
].map((x) => x);
[
  [10, 20],
  [20, 30],
  [30, 40],
].map((x) => x[0]);
//성이 3글자라는 전제를 하고 3글자씩만 뽑아내겠습니다.
["leehojun", "sinhojun", "kimhojun"].map((x) => x.slice(0, 3));
["leehojun", "sinhojun", "kimhojun"].map((v, i) => [v.slice(0, 3), i]);

// 아래처럼 값 뽑기.
[
  {
    name: "hojun",
    age: 10,
  },
  {
    name: "gildong",
    age: 20,
  },
].map((v) => v.age);

[
  {
    name: "hojun",
    age: 10,
  },
  {
    name: "gildong",
    age: 20,
  },
].map((v, i, obj) => {
  console.log(v, i, obj);
  return v;
});

// python : map(function, iterable)
// javascript : iterable.map(function)

let data = [
  {
    name: "lee hojun",
    age: 10,
  },
  {
    name: "kim junho",
    age: 20,
  },
  {
    name: "sin sunghun",
    age: 30,
  },
];

// 원하는 데이터
[
  [0, "hojun", 9],
  [1, "junho", 19],
  [2, "sunghun", 29],
];

data.map((v, i) => {
  let n = v["name"].split(" ")[1];
  let a = v["age"] - 1;
  return [i, n, a];
});

// unpacking
let aaaa = [1, 2, 3];
let bbbb = [10, 20, 30];
[...aaaa, 100, ...bbbb]; // (7) [1, 2, 3, 100, 10, 20, 30]
